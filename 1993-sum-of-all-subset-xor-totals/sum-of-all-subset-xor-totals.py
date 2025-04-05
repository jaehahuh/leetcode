class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, total_xor):
            if i == len(nums):
                return total_xor
            # include nums[i] and skip nums[i]
            return dfs (i + 1, total_xor ^ nums[i]) + dfs (i + 1, total_xor) 
        return dfs(0, 0)