class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for num in range(n, 101):
            temp = num
            prod = 1
            while temp > 0:
                prod *= temp % 10
                temp = temp//10
            if prod % t == 0:
                return num