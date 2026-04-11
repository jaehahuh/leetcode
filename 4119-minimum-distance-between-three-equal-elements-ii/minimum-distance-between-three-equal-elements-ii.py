class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        positions = defaultdict(list)
        for i, v in enumerate(nums):
            positions[v].append(i)
        
        found = False
        min_dist = float('inf')

        for v in positions:
            indices = positions[v]
            n = len(indices)
            if n < 3:
                continue
            
            found = True
            for i in range(n - 2):
                curr_dist = 2 * (indices[i+2] - indices[i])
                min_dist = min(min_dist, curr_dist)
        
        return min_dist if found else -1