class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        if nums[-1] < k:
            return -1
        
        operation = 0
        for i in range (1, len(nums)):
            if nums[i-1] > nums[i]:
                operation += 1
        return operation if k == nums[-1] else operation + 1