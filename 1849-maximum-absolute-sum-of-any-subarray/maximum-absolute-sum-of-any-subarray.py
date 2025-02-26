class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr_sum = 0
        pre_max = 0
        pre_min = 0
        max_sum = 0

        for num in nums:
            curr_sum += num
            pre_max = max(pre_max, curr_sum)
            pre_min = min(pre_min, curr_sum)
            max_sum = pre_max - pre_min
        
        return max_sum