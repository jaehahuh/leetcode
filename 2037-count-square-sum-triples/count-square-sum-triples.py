class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1, n+1):
            a2 = a * a
            for b in range(a+1, n+1):
                c2 = a2 + b*b
                c = math.isqrt(c2)
                if c * c == c2 and c <= n:
                    count += 2  # (a,b,c) and (b,a,c)
        return count