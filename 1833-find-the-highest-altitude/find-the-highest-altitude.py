class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        hightest = 0
        net_gain = 0
        for g in gain:
            net_gain += g
            hightest = max(hightest, net_gain)
        return hightest