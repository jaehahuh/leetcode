class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        majority = 0 # Store the dominant element
        count = 0 # Counts of the dominant element

        # Finding the dominant element using the Boyer-Moore Voting Algorithm
        for num in nums:
            if count == 0:
                majority = num # Set the current element as the dominant element
            
            if num == majority:
                count += 1
            else:
                count -= 1

        left_count = 0  # Count of the dominant element in the left part
        right_count = nums.count(majority) # Count of the dominant element in the right part

        for i in range(len(nums)):
            if nums[i] == majority:
                left_count += 1 # Increase left count if the current element is dominant
                right_count -= 1  # Decrease right count if the current element is dominant

            left_len = i + 1  # Length of the left part
            right_len = len(nums) - i - 1 # Length of the right part

            # Check the dominant element condition
            if 2 * left_count  > left_len and 2 * right_count > right_len:
                return i
                
        return -1 