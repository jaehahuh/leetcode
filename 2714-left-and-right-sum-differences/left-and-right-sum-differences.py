class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_sum = [0] * n
        right_sum = [0] * n
        result = []

        left_total = 0
        for i in range(n-1):
            left_total += nums[i]
            left_sum[i+1] = left_total
        
        right_total = 0
        for i in range(n-1, 0, -1):
            right_total += nums[i]
            right_sum[i-1] = right_total

        for i in range(n):
            result.append(abs(left_sum[i] - right_sum[i]))
        
        return result