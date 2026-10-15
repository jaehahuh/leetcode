class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        sum_squares = 0
        n = len(nums)
        for i in range(n):
            seen = set()
            distinct_count = 0
            for j in range(i, n):
                if nums[j] not in seen:
                    seen.add(nums[j])
                    distinct_count += 1
                sum_squares += distinct_count ** 2
        return sum_squares