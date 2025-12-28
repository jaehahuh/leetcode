class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        m = len(grid)
        n = len(grid[0])

        for r in range(m):
            for c in range(n - 1, -1, -1):
                if grid[r][c] < 0:
                    count += 1
                else:
                    break

        return count