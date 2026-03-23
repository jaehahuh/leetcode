class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        max_dp = [[None] * n for _ in range(m)]
        min_dp = [[None] * n for _ in range(m)]

        max_dp[0][0] = grid[0][0]
        min_dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                val = grid[i][j]
                candidates = []

                if i>0:
                    candidates.append((max_dp[i-1][j], min_dp[i-1][j]))
                if j>0:
                    candidates.append((max_dp[i][j-1], min_dp[i][j-1]))
                
                max_val = float('-inf')
                min_val = float('inf')

                for mx, mn in candidates:
                    if mx is None or mn is None:
                        continue
                    max_val = max(max_val, mx * val, mn * val)
                    min_val = min(min_val, mx * val, mn * val)
                
                max_dp[i][j] = max_val
                min_dp[i][j] = min_val
        
        if max_dp[m-1][n-1] is None or max_dp[m-1][n-1] < 0:
            return -1
        else:
            return max_dp[m-1][n-1] % MOD