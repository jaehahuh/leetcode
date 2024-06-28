class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        p1 = 0
        for p2 in range(1,len(nums)):
            #when p1 and p2 have different number, substitute the value of the p2 to the value of the p1
            if nums[p1] != nums[p2]:
                p1 += 1
                nums[p1] = nums[p2]
        
        #return numbers of unique elements in nums array 
        return p1 + 1
              
            
        
            