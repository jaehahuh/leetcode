class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        curr_num = 0 # Current base 10 value
        curr_len = 0 # Current subsequence length
        power_of_2 = 1

        for i in range(len(s)-1, -1, -1):
            ch = s[i]
            if ch == '0':
                curr_len += 1
                if power_of_2 <= k:
                    power_of_2 *= 2

            elif ch == '1':
                if curr_num + power_of_2 <= k:
                    curr_num += power_of_2
                    curr_len += 1
            
                if power_of_2 <= k:
                    power_of_2 *= 2
    
        return curr_len