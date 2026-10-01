class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in bracket_map:
                if not stack or stack.pop() != bracket_map[ch]:
                    return False
            else:
                stack.append(ch)
        
        return not stack