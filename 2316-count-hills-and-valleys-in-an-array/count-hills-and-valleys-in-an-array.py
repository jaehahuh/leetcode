class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        remove_dupli_nums = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                remove_dupli_nums.append(nums[i])

        if len(remove_dupli_nums) < 3: # There are no hills or valleys.
            return 0
        
        count_hill_valley = 0

        for i in range(1, len(remove_dupli_nums)-1):
            if remove_dupli_nums[i-1] < remove_dupli_nums[i] and remove_dupli_nums[i] > remove_dupli_nums[i + 1]:
                count_hill_valley += 1
            elif remove_dupli_nums[i-1] > remove_dupli_nums[i] and remove_dupli_nums[i] < remove_dupli_nums[i + 1]:
                count_hill_valley += 1
        
        return count_hill_valley