class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        num = 1
        while num < n:
            num *= 2
        return num == n