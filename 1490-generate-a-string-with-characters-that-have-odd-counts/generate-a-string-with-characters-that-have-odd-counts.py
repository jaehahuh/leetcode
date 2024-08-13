class Solution:
    def generateTheString(self, n: int) -> str:
        if n <= 0:
            return ''
        if n % 2 == 1:
            return 'x' * n
        else:
            return 'x' * (n-1) + 'y'