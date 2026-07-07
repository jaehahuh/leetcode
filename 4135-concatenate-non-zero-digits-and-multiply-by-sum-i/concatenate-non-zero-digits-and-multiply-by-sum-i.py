class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = ''
        sum = 0
        for digit in str(n):
            if digit != '0':
                x += digit
                sum += int(digit)
        if not x: 
            return 0
        return int(x) * sum