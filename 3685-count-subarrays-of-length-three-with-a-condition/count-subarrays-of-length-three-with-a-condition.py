class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        left = 0
        for right in range(2,len(nums)):
            if 2*(nums[left] + nums[right]) == nums[left+1]:
                count += 1
            left += 1

        return count