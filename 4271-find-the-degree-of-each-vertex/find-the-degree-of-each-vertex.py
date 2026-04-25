class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        result = [0] * n
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1:
                    result[i] += 1
        
        return result