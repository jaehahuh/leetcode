class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        #transpose
        for i in range(len(matrix)): 
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        #horizontal Flip after transpose
        for i in range(len(matrix)):
            matrix[i].reverse()