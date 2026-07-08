class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        P = [0] * (n + 1)
        S = [0] * (n + 1)
        cnt = [0] * (n + 1)
        
        for i in range(n):
            digit = int(s[i])
            if digit != 0:
                P[i+1] = (P[i] * 10 + digit) % MOD
                S[i+1] = S[i] + digit
                cnt[i+1] = cnt[i] + 1
            else:
                P[i+1] = P[i]
                S[i+1] = S[i]
                cnt[i+1] = cnt[i]
                
        power10 = [1] * (n + 1)
        for i in range(1, n + 1):
            power10[i] = (power10[i-1] * 10) % MOD

        result = []
        for l, r in queries:
            current_sum = S[r+1] - S[l]

            k = cnt[r+1] - cnt[l]
            
            if k == 0:
                result.append(0)
                continue
            x = (P[r+1] - P[l] * power10[k]) % MOD

            x = (x + MOD) % MOD
            
            ans = (x * current_sum) % MOD
            result.append(ans)
            
        return result