class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        #find the maximum element in the array
        max_num = max(nums)
        
        longest = 0
        curr_leng = 0

        #use Kadane's alogrithm
        for num in nums:
            if num == max_num:
                curr_leng += 1
                longest = max(longest, curr_leng)
            else:
                curr_leng = 0
        
        return longest