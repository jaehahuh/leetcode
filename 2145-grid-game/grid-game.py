class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # Initialize arrays to store the prefix sums for each row
        pre_row1 = grid[0].copy()
        pre_row2 = grid[1].copy()

        # Calculate the prefix sums
        for i in range (1, len(grid[0])):
            pre_row1[i] += pre_row1[i-1] # Update prefix sum for the first row
            pre_row2[i] += pre_row2[i-1] # Update prefix sum for the second row

        result = float('inf')
        # Iterate over each column to calculate the score for the second robot
        for i in range(len(grid[0])):
            # Calculate the score collected by the first robot if it stops at column i
            top_row = pre_row1[-1] - pre_row1[i]
            bottom_row = pre_row2[i - 1] if i > 0 else 0

            # Maximum points that the second robot can collect
            second_robot = max(top_row, bottom_row)
            # Update the result to minimize the points collected by the second robot
            result = min(result, second_robot)
        
        return result