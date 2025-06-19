class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        new_group_start = 0

        for i in range(len(nums)):
            if nums[i] - nums[new_group_start] > k:
                count += 1
                new_group_start = i
        
        return count + 1 # Include a last group