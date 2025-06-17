class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7

        # Precompute factorial and inverse factorial
        max_n = n
        factorial = [1] * (max_n + 1)
        inv_factorial = [1] * (max_n + 1)

        for i in range(1, max_n + 1):
            factorial[i] = factorial[i - 1] * i % MOD

        # Fermat's little theorem for inverse factorial
        inv_factorial[max_n] = pow(factorial[max_n], MOD - 2, MOD)
        for i in range(max_n - 1, -1, -1):
            inv_factorial[i] = inv_factorial[i + 1] * (i + 1) % MOD

        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return factorial[a] * inv_factorial[b] % MOD * inv_factorial[a - b] % MOD

        # Apply formula: C(n-1, k) * m * (m-1)^(n-1-k)
        result = comb(n - 1, k)
        result = result * m % MOD
        result = result * pow(m - 1, n - 1 - k, MOD) % MOD

        return result