class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(grid[0][0])

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                prev_xor_values = set()
                if r > 0:
                    prev_xor_values.update(dp[r - 1][c])
                if c > 0: 
                    prev_xor_values.update(dp[r][c - 1])

                val = grid[r][c]
                for prev_val in prev_xor_values:
                    dp[r][c].add(prev_val ^ val)
                    
        return min(dp[m - 1][n - 1])