class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sort array to avoid duplication
        answer = []
        
        for i, num1 in enumerate(nums):
            if i > 0 and num1 == nums[i-1]: #when number is duplicated in same position
                continue
            i_num2 = i + 1
            i_num3 = len(nums) - 1

            while i_num2 < i_num3:
                total = num1 + nums[i_num2] + nums[i_num3]
                if  total == 0:
                    answer.append([num1,nums[i_num2],nums[i_num3]])
                    i_num2 += 1
                    #when num2 index is duplicate then move 1 more index
                    while nums[i_num2] == nums[i_num2 - 1] and i_num2 < i_num3:
                        i_num2 += 1    

                elif total < 0:
                    i_num2 += 1
                
                else:
                     i_num3 -= 1
    
        return answer