class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def check_zero(num):
            return '0' in str(num)
        
        for a in range(1, n):
            b = n - a
            if not check_zero(a) and not check_zero(b):
                return [a, b]