class Solution:
    def coloredCells(self, n: int) -> int:
        return sum(4 * i for i in range(n)) + 1