class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum = 0
        result = []
        for n in nums:
            prefix_sum += n
            result.append(prefix_sum)
        
        return result