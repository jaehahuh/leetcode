class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odd_count = (high - low) //2
        if low % 2 == 1 or high % 2 == 1:
            odd_count += 1
        return odd_count