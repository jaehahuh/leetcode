class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7
        MAX = 20000  # 충분한 팩토리얼 범위 확보

        # 팩토리얼과 역팩토리얼 전처리
        fact = [1] * (MAX + 1)
        inv_fact = [1] * (MAX + 1)

        def modinv(x: int) -> int:
            return pow(x, MOD - 2, MOD)

        for i in range(1, MAX + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact[MAX] = modinv(fact[MAX])
        for i in range(MAX - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        def comb(n: int, r: int) -> int:
            if r < 0 or r > n:
                return 0
            return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

        def get_prime_factors(x: int) -> dict:
            # 소인수 분해 결과를 딕셔너리로 반환 (소수: 지수)
            factors = {}
            d = 2
            while d * d <= x:
                while x % d == 0:
                    factors[d] = factors.get(d, 0) + 1
                    x //= d
                d += 1
            if x > 1:
                factors[x] = factors.get(x, 0) + 1
            return factors

        total = 0
        for num in range(1, maxValue + 1):
            factors = get_prime_factors(num)
            count = 1

            # 각 소인수의 지수 e에 대해 중복조합 계산: comb(e + n - 1, e)
            for exponent in factors.values():
                count = count * comb(exponent + n - 1, exponent) % MOD

            total = (total + count) % MOD

        return total