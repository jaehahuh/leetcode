class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(n-1, -1 , -1):
            left, right = i-2, i-1
            if left < 0:
                continue
            if nums[i] < nums[left] + nums[right]:
                return nums[i] + nums[left] + nums[right]
        return 0