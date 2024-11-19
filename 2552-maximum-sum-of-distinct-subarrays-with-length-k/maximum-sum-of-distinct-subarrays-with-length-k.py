class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        current_sum = 0 
        max_sum = 0
        prev_idx = {}
        window_start = 0
        
        for window_end in range(len(nums)):
            current_sum += nums[window_end]
            i = prev_idx.get(nums[window_end], -1) #if key is exist, return nums[window_end], else return -1

            #remove the first number to keep the sliding window size in k
            while window_start <= i or  window_end - window_start + 1 > k:
                current_sum -= nums[window_start]
                window_start += 1
            
            #update max_sum when conditions are met
            if window_end - window_start + 1 == k:
                max_sum = max(max_sum, current_sum)
            prev_idx[nums[window_end]] = window_end

        return max_sum