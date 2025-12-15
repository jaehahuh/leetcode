class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10 ** 9 + 7
        s_indices = []
        for i, ch in enumerate(corridor):
            if ch == 'S':
                s_indices.append(i)
        
        n = len(s_indices)
        if n == 0 or n % 2 != 0:
            return 0
        
        ways_to_divide = 1

        for i in range(1, n - 1, 2):
            ways_to_divide = (ways_to_divide * (s_indices[i+1] - s_indices[i])) % MOD
        
        return ways_to_divide