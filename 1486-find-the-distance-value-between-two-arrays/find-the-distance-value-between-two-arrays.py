class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = len(arr1)
        for num1 in arr1:
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    count -= 1
                    break
        return count