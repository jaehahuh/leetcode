#find math pattern for O(1) time complexity 
# (num-1)%9 + 1 = (38 - 1)$9 + 1 = 37%9 + 1 = 1 + 1 = 2
class Solution:
    def addDigits(self, num: int) -> int:
        return (num-1)%9 + 1 if num != 0 else 0