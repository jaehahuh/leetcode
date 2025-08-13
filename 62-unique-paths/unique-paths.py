class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        for i in range(m):  # Initialize the first column (move straight down)
            dp[i][0] = 1
        
        for j in range(n):  # Initialize the first row (move straight right)
            dp[0][j] = 1
        
        # Each cell is the sum of top and left cells
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
        return dp[m-1][n-1] # Total number of unique paths