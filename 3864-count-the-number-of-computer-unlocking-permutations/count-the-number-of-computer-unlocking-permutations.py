class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        MOD = 10**9 + 7
        if n == 1:
            return 1
        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0

        result = math.factorial(n - 1) % MOD
        return result