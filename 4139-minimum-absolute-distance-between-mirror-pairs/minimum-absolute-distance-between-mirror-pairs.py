class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        last_seen = {}
        min_dist = float('inf')
        for j, num in enumerate(nums):
            if num in last_seen:
                dist = j-last_seen[num]
                if dist < min_dist:
                    min_dist = dist
            
            reversed_num = mirror_num = int(str(num)[::-1])
            last_seen[reversed_num] = j
        
        return min_dist if min_dist != float('inf') else -1