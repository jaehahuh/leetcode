class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1

        for i in range(n):
            if nums[i] < pivot:
                result[left] = nums[i]
                left += 1
        
        for i in range(n-1, -1, -1):
            if nums[i] > pivot:
                result[right] = nums[i]
                right -= 1
        
        while left <= right:
            result[left] = pivot
            left += 1
        
        return result