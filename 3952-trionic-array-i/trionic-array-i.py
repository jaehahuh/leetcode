class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        p = False
        q = False
        r = False # n - 1

        start = 0
        for i in range(start, len(nums)-1):
            if nums[i] < nums[i+1] and p == False:
                p = True
            elif nums[i] >= nums[i+1]:
                start = i
                break
        
        for i in range(start, len(nums)-1):
            if nums[i] > nums[i+1] and q == False:
                q = True
            elif nums[i] <= nums[i+1]:
                start = i
                break

        for i in range(start, len(nums)-1):
            if nums[i] < nums[i+1] and r == False:
                r = True
            elif nums[i] >= nums[i+1]:
                return False
        
        return True if (p == True and q == True and r == True) else False