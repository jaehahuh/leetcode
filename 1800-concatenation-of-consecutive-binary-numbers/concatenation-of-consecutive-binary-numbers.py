class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        result = 0
        length = 0
        for i in range(1, n+1):
            if (i & (i-1) == 0): # i가 2의 거듭제곱에 도달하면 이진수 길이 1 증가
                length += 1
            result = ((result << length) + i) % MOD
        return result