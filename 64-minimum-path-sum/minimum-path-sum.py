class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid) # row
        n = len(grid[0]) # col

        dp = [[0] * n for _ in range(m)] # Initialize a DP table of the same size as the grid

        dp[0][0] = grid[0][0] # Initialize the starting cell (0, 0)

        #first column of the DP table
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
    
        # first row of the DP table
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                # min(from top, from left) + current cell value
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]  

        # Return the minimum path sum to the bottom-right cell
        return dp[m-1][n-1]