class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = []
        count = 0

        for ch in s:
            if not stack:
                count += 1
                stack.append(ch)
            else:
                if ch != stack[-1]:
                    stack.pop()
                else:
                    stack.append(ch)
        
        return count