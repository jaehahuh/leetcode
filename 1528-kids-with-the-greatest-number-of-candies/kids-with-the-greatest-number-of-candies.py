class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = []
        max_candy = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candy:
                result.append(True)
            else:
                result.append(False)
        return result