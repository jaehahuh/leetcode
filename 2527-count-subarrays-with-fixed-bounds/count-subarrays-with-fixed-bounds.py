class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        last_minK = last_maxK = last_invalid = -1
        result = 0

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                last_invalid = i
            if num == minK:
                last_minK = i
            if num == maxK:
                last_maxK = i
            
            # Calculate the number of valid subarrays ending at current index
            valid_start = min(last_minK, last_maxK)
            if valid_start > last_invalid:
                result += valid_start - last_invalid

        return result