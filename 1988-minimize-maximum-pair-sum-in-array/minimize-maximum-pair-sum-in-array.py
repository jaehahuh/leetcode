class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        pair_sums = []
        nums.sort()
        n = len(nums)//2
        for i in range(n):
            pair_sum = nums[i] + nums[len(nums)-i-1]
            pair_sums.append(pair_sum)
        return max(pair_sums) 