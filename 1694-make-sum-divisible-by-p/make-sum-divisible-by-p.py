class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remainder = total % p

        if remainder == 0:
            return 0
        
        n = len(nums)
        result = n
        current_prefix_sum_remainder = 0

        remainder_map = {0: -1}  # remainder_map[0] = -1
        for i in range(n):
            current_prefix_sum_remainder = (current_prefix_sum_remainder + nums[i]) % p
            target_to_find = (current_prefix_sum_remainder - remainder + p) % p
            if target_to_find in remainder_map:
                current_subarray_len = i - remainder_map[target_to_find]
                result = min(result, current_subarray_len)   
            remainder_map[current_prefix_sum_remainder] = i

        if result == n:
            return -1
        else:
            return result