class Solution:
    def minInsertions(self, s: str) -> int:
        result = 0
        open_count = 0
        i = 0
        n = len(s)

        while i < n:
            if s[i] == '(':
                open_count += 1
                i += 1
            
            else:
                if i + 1 < n and s[i + 1] == ')':
                    i += 2
                
                else:
                    result += 1
                    i += 1
                
                if open_count > 0:
                    open_count -= 1
                else:
                    result += 1
        result += open_count * 2

        return result