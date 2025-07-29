class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        suffix_or = [0] * n
        if n > 0:
            suffix_or[n-1] = nums[n-1]
            for i in range(n-2, -1, -1):
                suffix_or[i] = nums[i] | suffix_or[i+1]
        
        last_pos_of_bit = [-1] * 30 

        for i in range(n - 1, -1, -1):
            for bit_index in range(30):
                if (nums[i] >> bit_index) & 1:
                    last_pos_of_bit[bit_index] = i
        
            target_or_value = suffix_or[i]
            min_end_index_needed = i

            for bit_idx in range(30):
                if (target_or_value >> bit_idx) & 1:
                    min_end_index_needed = max(min_end_index_needed, last_pos_of_bit[bit_idx])
            
            result[i] = min_end_index_needed - i + 1

        return result