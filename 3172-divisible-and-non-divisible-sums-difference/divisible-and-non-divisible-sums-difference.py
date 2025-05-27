class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n * (n+1) // 2
        num2 = 0   # Divisible sum of all integers in range [1, n]

        for num in range(m, n+1, m):
            num2 += num
        
        num1 = total - num2  # Not divisible sum

        return num1 - num2