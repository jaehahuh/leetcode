class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        # max - t = num - t
        # max = num + 2t
        return num + 2*t