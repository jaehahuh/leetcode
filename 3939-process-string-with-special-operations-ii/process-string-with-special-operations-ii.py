class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        lengths = [0] * n
        curr_len = 0

        for i in range(n):
            if s[i] == '*':
                curr_len = max(0, curr_len - 1)
            elif s[i] == '#':
                curr_len *= 2
            elif s[i] == '%':
                pass
            else:
                curr_len += 1
            lengths[i] = curr_len

        if not lengths or k >= lengths[-1]:
            return '.'
        
        target = k
        for i in range(n-1, -1, -1):
            char = s[i]
            len_after = lengths[i]
            len_before = lengths[i-1] if i > 0 else 0

            if char == '*':
                pass
            elif char == '#':
                if target >= len_before:
                    target %= len_before
            elif char == '%':
                target = len_before - 1 - target
            else:
                if target == len_after - 1:
                    return char
        
        return '.'