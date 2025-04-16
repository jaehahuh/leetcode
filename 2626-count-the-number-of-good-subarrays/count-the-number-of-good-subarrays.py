class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = 0   # Number of good subarrays
        number_counter = defaultdict(int) # Frequency hashmap of numbers in the current window
        pairs = 0  # Current number of (i, j) pairs where nums[i] == nums[j] and i < j
        left = 0

        for right in range(len(nums)):
            # Add the current number to the window and update pairs
            number_counter[nums[right]] += 1
            pairs += number_counter[nums[right]] - 1

            while pairs >= k:
                # All subarrays starting from left to right and ending at or after right are valid
                count += (len(nums) - right)
                
                # Remove the left number from the window and update pairs
                number_counter[nums[left]] -= 1
                if number_counter[nums[left]] > 0:
                    pairs -=  number_counter[nums[left]]
            
                left += 1
        
        return count