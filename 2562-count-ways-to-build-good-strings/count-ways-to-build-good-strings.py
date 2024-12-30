class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        dp = {}
        def backtracking(length):
            if length > high:
                return 0
            if length in dp:
                return dp[length]

            dp[length] = 1 if length >= low else 0
            dp[length] += backtracking(length + zero) + backtracking(length + one)

            return dp[length] % MOD
        return backtracking(0)