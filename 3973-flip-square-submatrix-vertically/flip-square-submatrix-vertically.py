class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(k//2):
            top_row = x + i
            bottom_row = x + k - i - 1

            for j in range(y, y + k):
                grid[top_row][j], grid[bottom_row][j] = grid[bottom_row][j], grid[top_row][j]
        
        return grid