class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n-1

        if nums[left] <= nums[right]:
            return nums[left]
        
        while left <= right:
            mid = (left + right)//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1