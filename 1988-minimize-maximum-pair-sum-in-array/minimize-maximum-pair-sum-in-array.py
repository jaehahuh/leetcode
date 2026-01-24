class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        max_pair_sum = 0
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            curr_pair_sum = nums[left] + nums[right]
            max_pair_sum = max(max_pair_sum, curr_pair_sum)
            left += 1
            right -= 1
        return max_pair_sum 