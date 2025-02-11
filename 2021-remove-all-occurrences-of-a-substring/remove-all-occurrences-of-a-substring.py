class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        s_stack = []
        for ch in s:
            s_stack.append(ch)
            if len(s_stack) >= len(part) and ''.join(s_stack[-len(part):]) == part:
                del s_stack[-len(part):]
            
        return ''.join(s_stack)