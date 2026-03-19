class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        result = 0
        rows, cols = len(grid), len(grid[0])
        
        prefix_x = [[0] * (cols + 1) for _ in range(rows + 1)]
        prefix_y = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for r in range(rows):
            for c in range(cols):
                prefix_x[r+1][c+1] = prefix_x[r][c+1] + prefix_x[r+1][c] - prefix_x[r][c] + (1 if grid[r][c] == 'X' else 0)
                prefix_y[r+1][c+1] = prefix_y[r][c+1] + prefix_y[r+1][c] - prefix_y[r][c] + (1 if grid[r][c] == 'Y' else 0)
                
                if prefix_x[r+1][c+1] > 0 and prefix_x[r+1][c+1] == prefix_y[r+1][c+1]:
                    result += 1

        return result 