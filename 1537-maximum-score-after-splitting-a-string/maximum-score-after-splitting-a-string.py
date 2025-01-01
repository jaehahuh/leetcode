class Solution:
    def maxScore(self, s: str) -> int:
        result = 0
        left_zero = 0
        right_one = s.count('1')
        for i in range(len(s)-1):
            if s[i] == '0':
                left_zero += 1
            else:
                right_one -= 1
            result = max(result, left_zero + right_one)
        return result