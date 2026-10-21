class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        if s == "".join(sorted(s)):
            return 0
 
        if n == 2:
            return -1
        
        max_alpha, min_alpha = max(s), min(s)

        if min_alpha == s[0] or max_alpha == s[-1]:
            return 1
        
        if any(c in [min_alpha, max_alpha] for c in s[1:-1]):
            return 2

        return 3