class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        max_k = -1

        for i, v in enumerate(nums):
            if i != v:
                max_k &= v

        return max(max_k, 0)