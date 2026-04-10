class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        positions = defaultdict(list)
        for i, v in enumerate(nums):
            positions[v].append(i)
        min_dist = float('inf')
        found = False

        for v in positions:
            indices = positions[v]
            if len(indices) < 3:
                continue
            
            found = True
            for i in range(len(indices) - 2):
                # (j - i) + (k - i) + (k - j) = 2(k - i)
                curr_dist = 2 * (indices[i+2] - indices[i])
                min_dist = min(min_dist, curr_dist)
            
        return min_dist if found else -1