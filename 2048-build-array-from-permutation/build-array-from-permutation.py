class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] += (nums[nums[i]] % len(nums)) * len(nums)
        for i in range(len(nums)):
            nums[i] //= len(nums) 
        return nums