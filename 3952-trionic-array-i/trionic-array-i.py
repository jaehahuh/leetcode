class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        
        def is_increasing(arr):
            return all(arr[i] < arr[i+1] for i in range(len(arr)-1))
        
        def is_decreasing(arr):
            return all(arr[i] > arr[i+1] for i in range(len(arr)-1))
        
        for p in range(1, n-2):
            for q in range(p+1, n-1):
                if (is_increasing(nums[0:p+1]) and 
                    is_decreasing(nums[p:q+1]) and
                    is_increasing(nums[q:n])):
                    return True
        return False