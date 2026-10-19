class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        result = []
        if target not in nums:
            return result
        
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
        
        return result