class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        partitions = 0
        right_prefix_sum = sum(nums)
        left_prefix_sum = 0
        for i in range(len(nums)-1):
            right_prefix_sum -= nums[i]
            left_prefix_sum += nums[i]
            if (right_prefix_sum - left_prefix_sum)% 2 == 0:
                partitions += 1
        return partitions