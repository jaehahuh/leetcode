class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        score_map = {0:0, 1:1, 2:2}
        cost_map = {0:0, 1:1, 2:1}

        dp = [[[-1]*(k+1) for _ in range(n)] for _ in range(m)]
        dp[0][0][0] = 0  # start_point
        
        for i in range(m):
            for j in range(n):
                cell_score = score_map[grid[i][j]]
                cell_cost = cost_map[grid[i][j]]
                if i == 0 and j == 0:
                    continue
                
                for cost_used in range(cell_cost, k+1):
                    max_score = -1
                    if i > 0 and dp[i-1][j][cost_used - cell_cost] != -1:
                        max_score = max(max_score, dp[i-1][j][cost_used - cell_cost] + cell_score)
                    if j > 0 and dp[i][j-1][cost_used - cell_cost] != -1:
                        max_score = max(max_score, dp[i][j-1][cost_used - cell_cost] + cell_score)
                    dp[i][j][cost_used] = max_score
            
        result = max(dp[m-1][n-1])
        return result if result != -1 else -1