from collections import Counter

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        stones_count = [0, 0, 0] # remainder (0,1,2)
        
        for stone in stones:
            stones_count[stone % 3] += 1
        
        r0, r1, r2 = stones_count[0], stones_count[1], stones_count[2]

        if r0 % 2 == 0:
            return min(r1, r2) >= 1
        else:
            return abs(r1 - r2) > 2