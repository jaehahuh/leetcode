class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = start
        for i in range(1, n):
            num = start + 2*i
            result = result ^ num
        return result