class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        for i in range(1, len(nums)):
            prev_parity = nums[i-1] % 2 
            curr_parity = nums[i] % 2
            if prev_parity == curr_parity:
                return False
        return True