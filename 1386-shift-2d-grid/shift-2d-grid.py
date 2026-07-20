class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m*n
        k = k % total
        result = [[0]*n for i in range(m)]

        for i in range(m):
            for j in range(n):
                new_index = (i*n + j + k) % total
                new_i = new_index//n
                new_j = new_index%n

                result[new_i][new_j] = grid[i][j]

        return result