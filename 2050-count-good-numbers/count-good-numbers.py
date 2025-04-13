class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        def pow(x, n):
            result = 1
            while n > 0:
                if n % 2:
                    result = (result * x) % MOD
                n = n//2
                x = (x * x) % MOD
            return result

        even = ceil(n/2)
        odd = n//2

        return (pow(5, even) * pow(4, odd)) % MOD