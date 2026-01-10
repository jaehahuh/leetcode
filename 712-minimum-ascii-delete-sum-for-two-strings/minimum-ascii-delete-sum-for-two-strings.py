class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        len1, len2 = len(s1), len(s2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        
        for i in range(1, len1 + 1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        
        for j in range(1, len2 + 1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])
        
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    cost_delete_s1 = ord(s1[i-1]) + dp[i-1][j]
                    cost_delete_s2 = ord(s2[j-1]) + dp[i][j-1]
                    dp[i][j] = min(cost_delete_s1, cost_delete_s2)
        
        return dp[len1][len2]