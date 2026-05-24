class Solution:
    def check(self, nums: List[int]) -> bool:
        size_window = 1
        if len(nums) == 1:
            return True

        for i in range(1, 2 * len(nums)):
            if nums[(i - 1) % len(nums)] <= nums[i % len(nums)]:
                size_window += 1
            else:
                size_window = 1
        
            if size_window == len(nums):
                return True
        return False