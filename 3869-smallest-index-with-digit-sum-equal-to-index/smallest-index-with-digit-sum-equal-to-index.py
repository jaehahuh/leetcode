class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            digit_sum = 0
            while nums[i] > 0:
                digit_sum += nums[i] % 10
                nums[i] //= 10
            if digit_sum == i:
                return i
        
        return -1