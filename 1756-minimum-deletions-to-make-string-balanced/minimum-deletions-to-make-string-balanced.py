class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        prefix_b = [0] * (n+1)
        for i in range(1, n+1):
            prefix_b[i] = prefix_b[i-1] + (1 if s[i-1] == 'b' else 0)

        suffix_a = [0] * (n+1)
        for i in range(n-1, -1, -1):
            suffix_a[i] = suffix_a[i+1] + (1 if s[i] == 'a' else 0) 

        min_del = float('inf')
        for i in range(n+1):
            min_del = min(min_del, prefix_b[i] + suffix_a[i])
        
        return min_del