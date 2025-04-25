class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        prefix_count = defaultdict(int) # To store frequency of prefix sums modulo values
        prefix_count[0] = 1 # Initial count for empty subarray

        prefix_sum = 0
        result = 0

        for num in nums:
            cnt = 1 if num % modulo == k else 0
            prefix_sum += cnt

            current_mod = prefix_sum % modulo # Current prefix sum modulo value

            # Calculate  the target modulo value for the condition to hold
            target_mod = (current_mod - k) % modulo    

            result += prefix_count[target_mod]

            prefix_count[current_mod] += 1
        
        return result