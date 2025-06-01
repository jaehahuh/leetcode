class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        result = 0
        for x in range(max(0, n - 2 * limit), min(limit, n) + 1):
            # y + z = n - x
            remain = n - x
            min_y = max(0, remain - limit)
            max_y = min(limit, remain)
            result += max_y - min_y + 1
        return result