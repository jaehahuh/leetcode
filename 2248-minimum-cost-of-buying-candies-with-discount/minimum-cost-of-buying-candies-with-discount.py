class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        return sum(candy for i, candy in enumerate(cost) if (i + 1) % 3 != 0)