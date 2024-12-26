class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums) #total number of elements in array
        dp = {} # (count, total)
        def backtrack(count, total):
            if (count, total) in dp:
                return dp[(count, total)]
            if count == n:
                if total == target:
                    return 1
                else:
                    return 0
            dp[(count, total)] = (backtrack(count+1, total + nums[count]) + 
            backtrack(count+1, total - nums[count]))

            return dp[(count, total)]

        return backtrack(0, 0)