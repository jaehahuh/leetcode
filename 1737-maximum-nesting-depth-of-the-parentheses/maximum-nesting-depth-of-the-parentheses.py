class Solution:
    def maxDepth(self, s: str) -> int:
        max_length = 0
        curr_depth = 0
        for ch in s:
            if ch == '(':
                curr_depth += 1
                if curr_depth > max_length:
                    max_length = curr_depth
            elif ch == ')':
                curr_depth -= 1
        return max_length