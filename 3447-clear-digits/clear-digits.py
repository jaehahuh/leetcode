class Solution:
    def clearDigits(self, s: str) -> str:
        char_stack = []
        for ch in s:
            if ch.isdigit() and char_stack:
                char_stack.pop()
            else:
                char_stack.append(ch)
        
        return ''.join(char_stack)