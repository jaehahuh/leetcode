class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1,61):
            remaining_sum = num1 - k * num2
            if remaining_sum < 0:
                if num2 > 0:
                    return -1
                else:
                    continue
            if remaining_sum >= k and remaining_sum.bit_count() <= k:
                return k
        return -1