class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0
        non_zero = False

        for num in nums:
            total_xor ^= num
            if num != 0:
                non_zero = True
        
        if not non_zero:
            return 0
        
        if total_xor != 0:
            return len(nums)
        
        return len(nums) - 1