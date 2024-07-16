#Sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_char = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in set_char:
                set_char.remove(s[left])
                left += 1
            set_char.add(s[right])
            max_len = max(max_len, right - left + 1)
        
        return max_len