class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        idx_x = 1
        idx_n = 1

        while idx_n <= n - 1:
            if idx_x & x == 0:
                if idx_n & (n-1):
                    res = res | idx_x
                idx_n = idx_n << 1

            idx_x <<= 1

        return res 