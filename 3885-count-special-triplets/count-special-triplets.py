class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        total_triplets = 0
        max_val = 2 * (10 ** 5)
        
        right_counts = [0] * (max_val + 1)
        for num in nums:
            right_counts[num] += 1
        
        left_counts = [0] * (max_val + 1)
        for j in range(n):
            curr_num = nums[j]
            right_counts[curr_num] -= 1
            target_val = curr_num * 2

            if target_val <= max_val:
                left_count = left_counts[target_val]
                right_count = right_counts[target_val]
                total_triplets = (total_triplets + (left_count * right_count)) % MOD
            
            left_counts[curr_num] += 1
            
        return total_triplets
