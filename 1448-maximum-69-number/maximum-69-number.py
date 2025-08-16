class Solution:
    def maximum69Number (self, num: int) -> int:
        result = str(num).replace('6','9', 1)
        return int(result)