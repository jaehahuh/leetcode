class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        check_unique = set()
        left = 0
        max_score = 0
        curr_sum = 0
        for right in range(len(nums)):
            # If the current number is already in the window, shrink from the left
            while nums[right] in check_unique:
                check_unique.remove(nums[left])
                curr_sum -= nums[left]
                left += 1
            
            # Add the current number to the window
            check_unique.add(nums[right])
            curr_sum  += nums[right]
            max_score = max(max_score, curr_sum)
        
        return max_score