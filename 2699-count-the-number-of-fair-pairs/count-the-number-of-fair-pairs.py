class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def binary_search(left,right,target):
            #return largest i, where nums[i] < target x
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return right

        nums.sort()
        res = 0
        for i in range(len(nums)):
            low = lower - nums[i]
            up = upper - nums[i]
            res += (binary_search(i+1,len(nums)-1, up + 1) - binary_search(i+1,len(nums)-1, low))
            
        return res