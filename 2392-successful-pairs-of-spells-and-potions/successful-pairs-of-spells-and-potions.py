class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = []
        potions.sort()
        n, m = len(spells), len(potions)
        for i in range(n):
            threshold = (success + spells[i] - 1) // spells[i]
            index = bisect.bisect_left(potions, threshold)
            result.append(m - index)
        return result