class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        #prefix sum
        total = sum(nums)
        remain = total % p

        # If the remainder is 0, no subarray needs to be removed
        if remain == 0:
            return 0
        
        res = len(nums)
        cur_sum = 0

        # map remain of prefix sums to last index
        remain_to_index = {0:-1} 
        for i, num in enumerate(nums):
            cur_sum = (cur_sum + num) % p
            prefix = (cur_sum - remain + p) %p

            # If there is a prefix with the same remainder, calculate the minimum subarray length
            if prefix in remain_to_index:
                length = i - remain_to_index[prefix]
                res = min(res, length)
            remain_to_index[cur_sum] = i
        
        # If the result is still the length of the array, return -1 (impossible case)
        if res == len(nums):
            return -1
        else:
            return res