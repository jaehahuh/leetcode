class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        min_val = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > min_val:
                max_diff = max(max_diff, nums[i]-min_val)
            else:
                min_val = nums[i]
        return max_diff