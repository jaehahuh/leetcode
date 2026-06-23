class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        k = r - l + 1
        up = [0] * (k+1)

        for i in range(1, k+1):
            up[i] = i - 1
        
        for i in range(3, n + 1):
            next_up = [0] * (k+1)
            for j in range(2, k+1):
                next_up[j] = (next_up[j-1] + up[k-j+2]) % MOD
            up = next_up
        
        total_valid = (2 * sum(up)) % MOD
        return total_valid