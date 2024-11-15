class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        #find longest array non-decreasing prefix
        left = 0
        while left < len(arr) - 1 and arr[left] <= arr[left+1]:
            left +=1

        # if the entire array is non-decreasing, no need to remove anything
        if left == len(arr) - 1:
            return 0

        #find the longest non-decreasing suffix
        right = len(arr)-1
        while right > 0 and arr[right] >= arr[right-1]:
            right -= 1
        
        # removing either prefix or suffix entirely
        res = min(len(arr)-left-1, right)
   
        i, j = 0, right
        while i <= left and j < len(arr):
            if arr[i] <= arr[j]:
                res = min(res, j - i - 1)
                i += 1
            else:
                j += 1
    
        return res 