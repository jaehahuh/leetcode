class Solution:
    def maxDepth(self, s: str) -> int:
        max_length = 0
        stack = []
        for ch in s:
            if ch == '(':
                stack.append('(')
                max_length = max(max_length, len(stack))
            elif ch == ')':
                stack.pop()
        
        return max_length