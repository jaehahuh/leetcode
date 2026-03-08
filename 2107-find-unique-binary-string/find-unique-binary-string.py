class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        num_set = set(nums)

        def backtracking(i, curr):
            if i == len(nums):
                result = ''.join(curr)
                return None if result in num_set else result
            
            result = backtracking(i+1, curr)
            if result:
                return result
            
            curr[i] = '1'
            result = backtracking(i+1, curr)
            if result:
                return result
            
        return backtracking(0, ['0' for n in nums])