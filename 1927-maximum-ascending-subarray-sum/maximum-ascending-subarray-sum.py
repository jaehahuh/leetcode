class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = current_sum 
        for i in range(1,len(nums)):
            if not nums[i] > nums[i-1]:
                current_sum = 0
            current_sum += nums[i]
            max_sum = max(max_sum, current_sum)
        return max_sum