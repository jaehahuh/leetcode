class Solution:
    def numSub(self, s: str) -> int:
        total_substrings = 0
        MOD = 10**9 + 7
        one_count = 0
        for i in range(len(s)):
            if s[i] == '1':
                one_count += 1
            else: 
                # (n * (n+1) / 2)
                total_substrings = (total_substrings + (one_count * (one_count + 1)) // 2) % MOD
                one_count = 0
        total_substrings = (total_substrings + (one_count * (one_count + 1)) // 2) % MOD

        return total_substrings