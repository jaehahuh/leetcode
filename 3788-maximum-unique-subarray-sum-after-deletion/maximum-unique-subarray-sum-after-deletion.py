class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_sum = 0
        count = 0
        for num in nums_set:
            if num >= 0:
                max_sum += num
                count += 1

        if count == 0:
            return max(nums_set)
        else:
            return max_sum
            