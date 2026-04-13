class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_dist = 1001 # Set minimum distance as 1001 since nums length <= 1000
        for i, num in enumerate(nums):
            if num == target:
                dist = abs(i - start)
                min_dist = min(min_dist, dist)
            
        return min_dist