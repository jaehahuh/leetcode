class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        inf = float('inf')
        dp = [[[-inf] * 3 for _ in range(n)] for _ in range(m)]

        for r in range(m):
            for c in range(n):
                val = coins[r][c]
                
                for k in range(3):
                    if r == 0 and c == 0:
                        dp[r][c][0] = val
                        if k > 0:
                            dp[r][c][k] = max(0, val) 
                        continue
                    
                    prev_max = -inf
                    if r > 0: prev_max = max(prev_max, dp[r-1][c][k])
                    if c > 0: prev_max = max(prev_max, dp[r][c-1][k])
                    
                    dp[r][c][k] = max(dp[r][c][k], prev_max + val)
         
                    if k > 0 and val < 0:
                        prev_k_max = -inf
                        if r > 0: prev_k_max = max(prev_k_max, dp[r-1][c][k-1])
                        if c > 0: prev_k_max = max(prev_k_max, dp[r][c-1][k-1])
                        dp[r][c][k] = max(dp[r][c][k], prev_k_max)

        return max(dp[m-1][n-1])