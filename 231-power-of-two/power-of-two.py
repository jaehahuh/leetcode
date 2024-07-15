class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #use bitwise &
        return n > 0 and (n & (n-1)) == 0