class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        abs_nums = []
        for num in nums:
            abs_nums.append(abs(num))
        abs_nums.sort()

        n = len(abs_nums)
        score = 0

        for i in range(n//2):
            score -= (abs_nums[i] ** 2)
        
        for i in range(n//2, n):
            score += (abs_nums[i] ** 2)

        return score