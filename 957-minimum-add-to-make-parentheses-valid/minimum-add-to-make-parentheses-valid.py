class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0
        for p in s:
            if p == "(":
                stack.append(p)
            elif p == ")" and len(stack) == 0:
                count += 1
            else:
                stack.pop()
        return len(stack) + count