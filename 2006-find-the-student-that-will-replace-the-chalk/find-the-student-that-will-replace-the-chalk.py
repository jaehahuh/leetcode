class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        k %= total 
        
        #O(n) Time complexity
        for i, count_chalk in enumerate(chalk):
            if k < count_chalk:
                return i
            k -= count_chalk