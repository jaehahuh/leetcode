class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_bit_num = max(nums)
        max_length = 0
        curr_length = 0

        for num in nums:
            if num == max_bit_num:
                curr_length += 1
                max_length = max(curr_length, max_length)
            else:
                curr_length = 0
        
        return max_length