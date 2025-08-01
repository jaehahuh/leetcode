class Solution:
    def pivotInteger(self, n: int) -> int:
        total = n * (n+1) // 2
        x = math.isqrt(total)
        if x * x == total and x <= n:
            return x
        else:
            return -1