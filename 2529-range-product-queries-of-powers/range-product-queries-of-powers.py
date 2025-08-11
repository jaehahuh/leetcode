class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        powers = []
        bit = 0
        num = n
        while num:
            if num & 1:
                powers.append(1 << bit)
            bit += 1
            num >>= 1

        result = []
        for left, right in queries:
            product = 1
            for i in range(left, right + 1):
                product = (product * powers[i]) % MOD
            result.append(product)
        return result