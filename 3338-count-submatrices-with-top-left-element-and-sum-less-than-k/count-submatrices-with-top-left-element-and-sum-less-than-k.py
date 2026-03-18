class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0]) #row, col
        prefix_sum = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                prefix_sum[r][c] = grid[r][c]
                if r > 0:
                    prefix_sum[r][c] += prefix_sum[r-1][c]
                if c > 0:
                    prefix_sum[r][c] += prefix_sum[r][c-1]
                if r > 0 and c > 0:
                    prefix_sum[r][c] -= prefix_sum[r-1][c-1]
        
        count = 0
        for r in range(m):
            for c in range(n):
                submat = prefix_sum[r][c]
                if submat <= k:
                    count += 1

        return count