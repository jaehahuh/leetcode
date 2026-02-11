
class LazyTag:
    def __init__(self):
        self.to_add = 0

    def merge(self, other: 'LazyTag') -> 'LazyTag':
        self.to_add += other.to_add
        return self

    def is_active(self) -> bool:
        return self.to_add != 0

    def reset(self):
        self.to_add = 0


class SegmentTreeNode:
    def __init__(self):
        self.min_value = 0
        self.max_value = 0
        self.lazy_tag = LazyTag()


class SegmentTree:
    def __init__(self, data: List[int]):
        self.n = len(data)
        self.tree = [SegmentTreeNode() for _ in range(self.n * 4 + 1)]
        self._build_tree(data, 1, self.n, 1)

    def range_add(self, left: int, right: int, val: int):
        tag = LazyTag()
        tag.to_add = val
        self._update_range(left, right, tag, 1, self.n, 1)

    def find_last_position(self, start: int, value: int) -> int:
        if start > self.n:
            return -1
        return self._query(start, self.n, value, 1, self.n, 1)

    def _apply_lazy(self, index: int, tag: LazyTag):
        node = self.tree[index]
        node.min_value += tag.to_add
        node.max_value += tag.to_add
        node.lazy_tag.merge(tag)

    def _push_down(self, index: int):
        node = self.tree[index]
        if node.lazy_tag.is_active():
            tag = LazyTag()
            tag.to_add = node.lazy_tag.to_add
            self._apply_lazy(index * 2, tag)
            self._apply_lazy(index * 2 + 1, tag)
            node.lazy_tag.reset()

    def _update_parent(self, index: int):
        left_child = self.tree[index * 2]
        right_child = self.tree[index * 2 + 1]
        node = self.tree[index]
        node.min_value = min(left_child.min_value, right_child.min_value)
        node.max_value = max(left_child.max_value, right_child.max_value)

    def _build_tree(self, data: List[int], left: int, right: int, index: int):
        if left == right:
            node = self.tree[index]
            node.min_value = data[left - 1]
            node.max_value = data[left - 1]
            return

        mid = (left + right) >> 1
        self._build_tree(data, left, mid, index * 2)
        self._build_tree(data, mid + 1, right, index * 2 + 1)
        self._update_parent(index)

    def _update_range(self, target_left: int, target_right: int, tag: LazyTag,
                      left: int, right: int, index: int):
        if target_left <= left and right <= target_right:
            self._apply_lazy(index, tag)
            return

        self._push_down(index)
        mid = (left + right) >> 1

        if target_left <= mid:
            self._update_range(target_left, target_right, tag, left, mid, index * 2)
        if target_right > mid:
            self._update_range(target_left, target_right, tag, mid + 1, right, index * 2 + 1)

        self._update_parent(index)

    def _query(self, target_left: int, target_right: int, value: int,
               left: int, right: int, index: int) -> int:
        node = self.tree[index]
        # 구간 최소값이 value보다 크거나 최대값이 value보다 작으면 조건 만족 불가
        if node.min_value > value or node.max_value < value:
            return -1

        if left == right:
            return left

        self._push_down(index)
        mid = (left + right) >> 1

        # 오른쪽 자식부터 탐색해서 더 오른쪽 위치 찾기 (last 위치 찾기)
        if target_right >= mid + 1:
            res = self._query(target_left, target_right, value, mid + 1, right, index * 2 + 1)
            if res != -1:
                return res

        if target_left <= mid:
            return self._query(target_left, target_right, value, left, mid, index * 2)

        return -1


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        # 각 숫자별 등장 위치 저장 (1-based index)
        occurrences: defaultdict[int, deque[int]] = defaultdict(deque)

        def sign(x: int) -> int:
            # 짝수면 +1, 홀수면 -1 리턴
            return 1 if x % 2 == 0 else -1

        n = len(nums)
        prefix_sum = [0] * n
        prefix_sum[0] = sign(nums[0])
        occurrences[nums[0]].append(1)

        # prefix_sum 계산: nums[i]가 첫 등장 시 부호 추가, 아니면 부호 미변경
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1]
            if not occurrences[nums[i]]:
                prefix_sum[i] += sign(nums[i])
            occurrences[nums[i]].append(i + 1)

        seg_tree = SegmentTree(prefix_sum)
        max_length = 0

        for i in range(n):
            # 현재 최대 길이 이후 위치부터 값이 0인 가장 오른쪽 위치 찾음
            candidate_pos = seg_tree.find_last_position(i + max_length + 1, 0)
            if candidate_pos != -1:
                max_length = max(max_length, candidate_pos - i)

            # 현재 인덱스 i의 숫자 등장 위치에서 제거 (앞에서부터)
            occurrences[nums[i]].popleft()
            next_occurrence = occurrences[nums[i]][0] if occurrences[nums[i]] else n + 1

            # i+1 ~ next_occurrence-1 구간에 대해 prefix_sum 값 보정 (부호 빼기)
            seg_tree.range_add(i + 1, next_occurrence - 1, -sign(nums[i]))

        return max_length