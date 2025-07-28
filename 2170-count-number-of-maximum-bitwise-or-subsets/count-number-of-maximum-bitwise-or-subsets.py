class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num
        
        n = len(nums)
        count = 0
        for i in range(1 << n):
            current_or_sum = 0
            for j in range(n):
                if (i >> j) & 1:
                    current_or_sum |= nums[j]
            
            if current_or_sum == max_or:
                count += 1
        
        return count