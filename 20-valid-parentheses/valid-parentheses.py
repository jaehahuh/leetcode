class Solution:
    def isValid(self, s: str) -> bool:
        order = {
            ")":"(",
            "]":"[",
            "}":"{"}
        
        stack = []
        for ch in s:
            if ch not in order:
                stack.append(ch)
            elif not stack or order[ch] != stack.pop():
                return False

        if len(stack) == 0:
            return True
