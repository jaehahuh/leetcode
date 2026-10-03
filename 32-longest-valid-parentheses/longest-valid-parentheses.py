class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        
        n = len(s)
        dp = [0] * n
        longest = 0

        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2

                elif i - 1 - dp[i-1] >= 0 and s[i - 1 - dp[i-1]] == '(':
                    prev_len = dp[i-1]
                    outer_len = dp[i - 2 - dp[i - 1]] if i - 2 - dp[i - 1] >= 0 else 0
                    dp[i] = prev_len + 2 + outer_len
                
                longest = max(longest, dp[i])
        return longest