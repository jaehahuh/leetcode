class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        result = ''
        count = 0
        left = 0
        n = len(s)
        for right in range(n):
            if s[right] == '1':
                count += 1
            while count == k:
                sub = s[left:right + 1]
            
                if not result or len(sub) < len(result) or ((len(sub) == len(result)) and sub < result):
                    result = sub

                if s[left] == '1':
                    count -= 1
                left += 1
        
        return result