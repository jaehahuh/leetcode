class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[0] * (i + 1) for i in range(numRows)]

        for i in range(numRows):
            for j in range(i + 1):
                if j == 0 or j == i:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

        return dp