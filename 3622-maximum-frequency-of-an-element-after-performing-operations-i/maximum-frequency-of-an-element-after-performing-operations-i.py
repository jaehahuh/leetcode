class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        count_dict = Counter(nums)
        min_val = min(nums)
        max_val = max(nums)

        # 배열 범위: [min_val - k, max_val + k]
        left_bound = min_val - k
        right_bound = max_val + k

        # 오프셋을 사용하여 음수 인덱스 방지
        offset = -left_bound  # left_bound + offset = 0
        size = right_bound + offset + 2  # right_bound + 1까지 접근 가능하도록 여유 둠

        diff = [0] * size
        # 각 원소의 구간 [a-k, a+k]에 대해 diff 배열에 이벤트 추가
        for a in nums:
            L = a - k + offset
            R = a + k + offset
            diff[L] += 1
            diff[R + 1] -= 1

        # 누적합으로 각 정수 t에서의 overlap 계산
        overlap = [0] * size
        cur = 0
        for i in range(size):
            cur += diff[i]
            overlap[i] = cur

        ans = 0
        # 모든 가능한 t에 대해 candidate 계산
        # t를 실제 정수 값으로 변환: t = i - offset
        for i in range(size):
            t = i - offset
            # exact: t가 nums에 있으면 count_dict[t] else 0
            exact = count_dict.get(t, 0)
            total_in_range = overlap[i]  # t를 포함하는 구간의 수
            convertible = total_in_range - exact
            if convertible < 0:
                convertible = 0
            candidate = exact + min(numOperations, convertible)
            if candidate > ans:
                ans = candidate

        return ans