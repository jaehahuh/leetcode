class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, -float('inf'), -float('inf')] #remainder :[0, 1, 2]
        for num in nums:
            prev_dp = list(dp)
            for i in range(3):
                if prev_dp[i] == -float('inf'):
                    continue
                new_sum = prev_dp[i] + num
                new_remain = new_sum % 3

                dp[new_remain] = max(dp[new_remain], new_sum)
        
        return dp[0]