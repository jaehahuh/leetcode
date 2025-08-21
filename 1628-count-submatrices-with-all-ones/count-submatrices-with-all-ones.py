class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        dp = [[0] * n for _ in range(m)]

        count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if i > 0:
                        dp[i][j] = dp[i-1][j] + 1
                    else:
                        dp[i][j] = 1
        
                    min_height = dp[i][j]
                    for k in range(j, -1, -1):
                        min_height = min(min_height, dp[i][k])
                        count += min_height
                else:
                    dp[i][j] = 0
        return count