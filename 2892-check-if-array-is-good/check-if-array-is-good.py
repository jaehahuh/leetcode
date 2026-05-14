class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        nums.sort()
        if n < 2:
            return False
            
        if nums[0] != 1:
            return False

        for i in range(1, n-1):
            if nums[i] != nums[i-1] + 1:
                return False

        if nums[n-2] != nums[n-1]:
            return False

        return True