class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums_set = set(nums)
        positives = [num for num in nums_set if num >= 0]
        return sum(positives) if positives else max(nums_set)