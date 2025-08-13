class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        T = [0] * (n + 1)

        T[0] = 0
        T[1] = 1
        T[2] = 1

        for i in range(3, n + 1):
            T[i] = T[i-1] + T[i-2] + T[i-3]
        
        return T[n]