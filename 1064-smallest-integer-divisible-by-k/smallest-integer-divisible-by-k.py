class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1

        remainder = 0
        length = 0
        while True:
            length += 1
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length