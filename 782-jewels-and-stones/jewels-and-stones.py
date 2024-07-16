import collections

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total = 0
        counter = collections.Counter(stones)
        for jewel in jewels:
            total += counter[jewel] 
        return total