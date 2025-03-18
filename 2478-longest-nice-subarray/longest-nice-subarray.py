class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        longest_length = 0
        current_bitmask = 0
        left = 0
        for right in range(len(nums)):
            # While there is a bit overlap with the current number
            while current_bitmask & nums[right]:
                current_bitmask ^= nums[left]
                left += 1

            # Update the max length
            longest_length = max(longest_length, right - left + 1)
            # Add the current number to the bitmask
            current_bitmask |= nums[right]

        return longest_length