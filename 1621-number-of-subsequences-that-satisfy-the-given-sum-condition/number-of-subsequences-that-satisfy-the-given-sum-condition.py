class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        nums.sort()
        count = 0

        left = 0
        right = n - 1
        
        powers = [1] * n # powers[0] = 2^0 = 1
        for i in range(1, n):
            powers[i] = (powers[i-1] * 2) % MOD
        
        while left <= right:
            if nums[left] + nums[right] <= target:
                count = (count + powers[right-left]) % MOD
                left += 1
            else:
                right -= 1
        
        return count