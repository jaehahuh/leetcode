class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        move = 0
        for ch in s:
            if ch == '(':
                stack.append('(')
            else:
                if stack:
                    stack.pop()
                else:
                    move += 1

        return len(stack) + move