class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd, sumEven = 0,0
        for i in range(n):
            sumOdd += 2*i - 1
            sumEven += 2*i
        return math.gcd(sumOdd, sumEven)  