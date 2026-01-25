# Sort and then Sliding Window
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        if k == 1:
            return 0
        
        min_diff = float('inf')

        for left in range(n-k+1):
            right = left + k - 1
            for i in range(left, right):
                curr_diff = nums[right]-nums[left]
                min_diff = min(min_diff, curr_diff)

        return min_diff