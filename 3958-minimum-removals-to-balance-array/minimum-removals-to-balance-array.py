class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = 0
        max_length = 1
        
        for end in range(len(nums)):
            while nums[end] > nums[start] * k:
                start += 1
            max_length = max(max_length, end-start+1)
        
        return len(nums) - max_length