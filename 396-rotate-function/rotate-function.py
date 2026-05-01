class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)

        current_f = sum(i * num for i, num in enumerate(nums)) # F(0)
        max_f = current_f

        for k in range(1,n):
            # Recurrence Relation: F(k) = F(k-1) + sum - n * nums[n-k]
            current_f = current_f + total - n * nums[n-k]
            if current_f > max_f:
                max_f = current_f
        
        return max_f