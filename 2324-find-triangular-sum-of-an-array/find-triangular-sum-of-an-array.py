class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        i, j = 0, 1
        while n != 1:
            nums[i] = (nums[i] + nums[j]) % 10
            i += 1
            j += 1
            if j == n:
                nums.pop()
                i = 0
                j = 1
                n -= 1
                
        return nums[0]