class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        num_set = set(nums)
        seq_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                seq_sum += nums[i]
            else:
                break

        while seq_sum in num_set:
            seq_sum += 1

        return seq_sum