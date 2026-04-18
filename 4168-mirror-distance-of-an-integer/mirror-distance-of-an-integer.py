class Solution:
    def mirrorDistance(self, n: int) -> int:
        mirror_num = int(str(n)[::-1])
        return abs(n-mirror_num)