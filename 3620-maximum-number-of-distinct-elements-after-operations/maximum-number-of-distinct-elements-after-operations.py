class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 0:
            return len(set(nums))

        intervals = []
        for num in nums:
            intervals.append((num-k, num+k))
        
        # Sort by right end
        intervals.sort(key=lambda x: x[1])
        last_assigned = -float('inf')
        count = 0
        
        for l, r in intervals:
            candidate = max(l, last_assigned + 1)
            if candidate <= r:
                count += 1
                last_assigned = candidate
        
        return count