class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc_length = 1 
        dec_length = 1  
        max_inc = 1
        max_dec = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dec_length = 1  # reset decreasing length
                inc_length += 1
            elif nums[i] < nums[i-1]:
                inc_length = 1  # reset increasing length
                dec_length += 1
            else:
                # if equal values, reset both counts
                inc_length = 1
                dec_length = 1
            
            # update maximum lengths
            max_inc = max(max_inc, inc_length)
            max_dec = max(max_dec, dec_length)
            
        return max(max_inc, max_dec)