class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # since it is an n x n matrix, row and column are the same
        n = len(grid)
        result = [[0] * (n-2) for _ in range(n-2)]
       
        for i in range(n-2):
            for j in range(n-2):
                #find the largest value in every contiguous 3 x 3
                for column in range(i, i+3):
                    for row in range(j, j+3):
                        result[i][j] = max(result[i][j], grid[column][row])

        return result 