class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        #counting sort method
        #create a frequency array (constrains: 0 < nums[i] < 100), so set freq list size as 101 
        freq = [0] * 101

        #count frequency
        for num in nums:
            freq[num] += 1
        
        
        #convert frequency array to prefix sum array
        for i in range(1, 101):
            freq[i] += freq[i - 1]
        

        result = []
        for num in nums:
            if num == 0:
                result.append(0)
            else:
                result.append(freq[num - 1])
        
        return result