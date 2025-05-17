class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        pointer = 0
        end = len(nums) - 1

        while pointer <= end:
            if nums[pointer] == 0:
                nums[start], nums[pointer] = nums[pointer], nums[start]
                start += 1
                pointer += 1
            
            elif nums[pointer] == 1:
                pointer += 1
            
            else: #nums[pointer] == 2
                nums[end], nums[pointer] = nums[pointer], nums[end]
                end -= 1