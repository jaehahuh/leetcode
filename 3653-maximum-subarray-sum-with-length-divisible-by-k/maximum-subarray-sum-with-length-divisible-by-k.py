class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        min_prefix_sums_by_remainder = {0: 0}
        max_sum = -float('inf')
        prefix_sum = 0
        
        for i, num in enumerate(nums, 1):
            prefix_sum += num
            current_index_remainder = (i % k + k) % k

            if current_index_remainder in min_prefix_sums_by_remainder:
                max_sum = max(max_sum, prefix_sum - min_prefix_sums_by_remainder[current_index_remainder])
            min_prefix_sums_by_remainder[current_index_remainder] = min(min_prefix_sums_by_remainder.get(current_index_remainder, float('inf')), prefix_sum)
        
        return max_sum