class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        # Build suffix minimums
        suffix_min = [''] * n
        suffix_min[-1] = s[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(s[i], suffix_min[i + 1])

        stack = []
        result = []
        
        for i in range(n):
            stack.append(s[i])
            
            # Pop from stack while possible
            while stack and (i == n - 1 or stack[-1] <= suffix_min[i + 1]):
                result.append(stack.pop())
        
        return ''.join(result)