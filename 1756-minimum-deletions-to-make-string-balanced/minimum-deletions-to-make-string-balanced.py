class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack = []
        min_del = 0
        for ch in s:
            if ch == 'a' and stack and stack[-1] == 'b':
                stack.pop()
                min_del += 1
            else:
                stack.append(ch)
            
        return min_del