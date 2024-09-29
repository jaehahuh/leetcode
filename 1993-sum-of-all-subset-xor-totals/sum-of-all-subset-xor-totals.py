class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        
        def backtrack(i, curr_xor):
            nonlocal total
            total += curr_xor

            # explore the subsets starting from the current index
            for i in range(i, len(nums)):
                backtrack (i+1, curr_xor ^ nums[i])

        backtrack(0, 0)
        return total 
        