class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        max_diff = -1 # Since it is absolue difference, the answer must be positive

        for i in range(n):
            diff = abs(nums[i] - nums[(i + 1) % n])
            max_diff = max(max_diff, diff)
 
        return max_diff