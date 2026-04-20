class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        max_dist = 0
        for right in range(n-1, 0, -1):
            if colors[0] != colors[right]:
                max_dist = max(max_dist, right)
                break
        
        for left in range(1, n-1):
            if colors[left] != colors[n-1]:
                max_dist = max(max_dist, n-1-left)
                break
        
        return max_dist