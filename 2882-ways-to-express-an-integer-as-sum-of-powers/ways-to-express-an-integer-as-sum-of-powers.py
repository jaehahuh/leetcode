class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        powers = []
        num = 1
        while True:
            p = num ** x
            if p > n:
                break
            powers.append(p)
            num += 1
            
        dp = [0] * (n + 1)
        dp[0] = 1 # One way to make 0: choose nothing

        # For each power p, update in descending order to ensure each p is used at most once
        for p in powers:
            for i in range(n, p-1, -1):
                dp[i] = (dp[i] + dp[i-p]) % MOD
        
        return dp[n]