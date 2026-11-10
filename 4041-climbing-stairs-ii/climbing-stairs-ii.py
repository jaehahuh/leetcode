class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n+1):
            for j in range(1, 4):
                if i - j >= 0:
                    jump_cost = costs[i - 1] + (j ** 2)
                    dp[i] = min(dp[i], dp[i-j] + jump_cost)
        
        return dp[n]