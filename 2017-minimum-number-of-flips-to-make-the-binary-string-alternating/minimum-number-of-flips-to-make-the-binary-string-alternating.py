class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        doubled_s = s+s
        
        pattern1 = ''.join('0' if i % 2 == 0 else '1' for i in range(2 * n)) # start with 0
        pattern2 = ''.join('1' if i % 2 == 0 else '0' for i in range(2 * n)) # start with 1

        diff1 = 0
        diff2 = 0

        result = float('inf')

        for i in range(2 * n):
            if doubled_s[i] != pattern1[i]:
                diff1 += 1
            if doubled_s[i] != pattern2[i]:
                diff2 += 1
        
            if i >= n:
                if doubled_s[i - n] != pattern1[i - n]:
                    diff1 -= 1
                if doubled_s[i - n] != pattern2[i - n]:
                    diff2 -= 1
            
            if i >= n - 1:
                result = min(result, diff1, diff2)
        
        return result