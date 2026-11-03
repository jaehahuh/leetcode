class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[-1] - num for num in nums)