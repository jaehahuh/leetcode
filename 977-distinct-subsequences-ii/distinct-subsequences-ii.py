class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        last_added_by_char = [0] * 26
        total = 0
        for ch in s:
            i = ord(ch) - ord('a')
            new_subsequences = ((total + 1) - (last_added_by_char[i])) % MOD
            total = (total + new_subsequences) % MOD
            last_added_by_char[i] = (last_added_by_char[i] + new_subsequences) % MOD
        
        return total