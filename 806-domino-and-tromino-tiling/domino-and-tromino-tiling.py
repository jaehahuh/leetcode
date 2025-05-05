class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n+1)
        dp[0] = 1 # Ways to tile a 2 x 0 board (empty board)
        dp[1] = 1 # Ways to tile a 2 x 1 board
        dp[2] = 2 # Ways to tile a 2 x 2 board (based on this specific recurrence)

        for i in range(3, n + 1):
            dp[i] = (2 * dp[i-1] + dp[i-3]) % MOD # Apply the recurrence relation: dp[i] = 2 * dp[i-1] + dp[i-3]
        
        return dp[n]