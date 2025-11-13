class Solution:
    def maxOperations(self, s: str) -> int:
        operations = 0
        count_ones = 0
        for i in range(len(s)):
            if s[i] == '1':
                count_ones += 1 
            elif s[i] == '0':
                if count_ones > 0 and (i > 0 and s[i-1] == '1'):
                    operations += count_ones

        return operations