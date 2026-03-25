class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        r, c = len(grid), len(grid[0])
        prefix_sum = sum(num for row in grid for num in row)
        
        #Horizontal cut
        horizontal_sum = 0
        for row in grid:
            horizontal_sum += sum(row)
            if horizontal_sum == prefix_sum - horizontal_sum:
                return True 
            if horizontal_sum > prefix_sum - horizontal_sum:
                break
        
        #Vertical cut
        vertical_sum = 0
        for i in range(c):
            for row in grid:
                vertical_sum += row[i]
            if vertical_sum == prefix_sum - vertical_sum:
                return True 
            if vertical_sum > prefix_sum - vertical_sum:
                break

        return False