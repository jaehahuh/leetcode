class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        num_set = set(nums)

        def backtrack(i, curr_num):
            if i == len(nums):
                result =  ''.join(curr_num)
                return None if result in num_set else result
            
            result = backtrack(i+1, curr_num)
            if result:
                return result
            
            curr_num[i] = "1"
            result = backtrack(i+1, curr_num)
            if result:
                return result
    
        return backtrack(0, ["0" for n in nums])