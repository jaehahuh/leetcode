class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        # Calculate the height of consecutive ones in each column up to current row
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]
        
        max_area = 0

        for i in range(m):
            heights = sorted(matrix[i], reverse=True) # Sort the heights in descending order to simulate column rearrangement
            for width in range(1, n+1):
                area = heights[width-1] * width # Calculate the maximum possible area for each possible width
                if area > max_area: 
                    max_area = area
        
        return max_area