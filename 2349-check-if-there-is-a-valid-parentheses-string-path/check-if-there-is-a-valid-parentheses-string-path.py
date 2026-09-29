class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        if (m + n - 1) % 2 != 0:
            return False
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False
        
        dp = [[set() for _ in range(n)] for _ in range(m)]

        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):
                if not dp[i][j]:
                    continue
                
                for b in dp[i][j]:
                    # move downward
                    if i + 1 < m:
                        next_b = b + (1 if grid[i+1][j] == '(' else -1)
                        if next_b >= 0:
                            rem = (m - 1 - (i + 1)) + (n - 1 - j)
                            if next_b <= rem:
                                dp[i + 1][j].add(next_b)

                    # move leftward
                    if j + 1 < n:
                        next_b = b + (1 if grid[i][j + 1] == "(" else -1)
                        if next_b >= 0:
                            rem = (m - 1 - i) + (n - 1 - (j + 1))
                            if next_b <= rem:
                                dp[i][j + 1].add(next_b)

        return 0 in dp[m-1][n-1]