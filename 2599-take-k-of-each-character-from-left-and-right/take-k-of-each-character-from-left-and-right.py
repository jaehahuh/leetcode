class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        #Total counts
        count = [0, 0, 0] #a,b,c
        for ch in s:
            count[ord(ch)-ord('a')] += 1
        
        if min(count) < k:
            return -1
      
        #silding window
        res = float('inf')
        left = 0
        for right in range(len(s)):
            count[ord(s[right]) - ord('a')] -= 1

            while min(count) < k:
                count[ord(s[left]) - ord('a')] += 1
                left += 1
            res = min(res, len(s) - (right - left + 1))
        
        return res