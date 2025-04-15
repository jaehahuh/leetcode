class Solution:
    class BinaryIndexedTree:
        """
        1-indexed Fenwick Tree (Binary Indexed Tree) 자료구조
        - point update: 특정 인덱스의 값을 delta만큼 증가
        - prefix sum query: 0부터 index까지의 누적합 반환
        """
        def __init__(self, size: int):
            # 내부적으로 1부터 size까지 사용하므로 배열 크기를 size+1로 설정
            self.size = size
            self.tree = [0] * (size + 1)

        def update(self, index: int, delta: int) -> None:
            """
            index 위치에 delta만큼 더하기
            (외부에서 0-based 인덱스를 전달하면 내부에서 1-based로 변환)
            """
            i = index + 1  # 1-based 인덱스로 변환
            while i <= self.size:
                self.tree[i] += delta
                i += i & -i  # 다음 갱신할 노드로 이동

        def prefix_sum(self, index: int) -> int:
            """
            0부터 index까지의 합을 반환
            (외부에서 0-based 인덱스를 전달하면 내부에서 1-based로 변환)
            """
            i = index + 1  # 1-based 인덱스로 변환
            result = 0
            while i > 0:
                result += self.tree[i]
                i -= i & -i  # 부모 노드로 이동
            return result

    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        # 1) nums2 배열에서 각 값(value)이 등장하는 인덱스(position)를 기록
        #    index_in_nums2[val] = nums2에서 val이 위치한 인덱스
        index_in_nums2 = [0] * n
        for position, value in enumerate(nums2):
            index_in_nums2[value] = position

        # 2) nums1을 순회하면서, 각 값(value)을 nums2에서의 인덱스(position)로 치환
        #    mapped_positions[i] = nums2 상에서 nums1[i]가 위치한 인덱스
        mapped_positions = [index_in_nums2[value] for value in nums1]

        # 3) 왼쪽 구간에서 나보다 작은(mapped_positions[j]보다 작은) 원소 개수 세기
        bit_left = self.BinaryIndexedTree(n)
        smaller_count_left = [0] * n
        for j in range(n):
            pos = mapped_positions[j]
            if pos > 0:
                # [0 .. pos-1] 구간의 누적합 = 나보다 작은 값의 개수
                smaller_count_left[j] = bit_left.prefix_sum(pos - 1)
            # 현재 위치 pos의 값을 1 증가시켜 이후 쿼리에서 반영되도록 함
            bit_left.update(pos, 1)

        # 4) 오른쪽 구간에서 나보다 큰(mapped_positions[j]보다 큰) 원소 개수 세기
        bit_right = self.BinaryIndexedTree(n)
        larger_count_right = [0] * n
        for j in range(n - 1, -1, -1):
            pos = mapped_positions[j]
            # 전체 오른쪽에 있는 원소 개수 = [0 .. n-1] 누적합
            total_on_right = bit_right.prefix_sum(n - 1)
            # [0 .. pos]까지의 누적합 = 오른쪽에서 나보다 작거나 같은 값의 개수
            count_up_to_pos = bit_right.prefix_sum(pos)
            # 차이를 통해 나보다 큰 값의 개수 계산
            larger_count_right[j] = total_on_right - count_up_to_pos
            # 현재 위치 pos의 값을 1 증가시켜 이후 쿼리에서 반영되도록 함
            bit_right.update(pos, 1)

        # 5) 각 인덱스 j를 중간값으로 삼는 좋은 트리플릿 개수 합산
        #    중간값 j 기준으로: 왼쪽에 더 작은 값 * 오른쪽에 더 큰 값
        good_triplets_count = 0
        for j in range(n):
            good_triplets_count += smaller_count_left[j] * larger_count_right[j]

        return good_triplets_count