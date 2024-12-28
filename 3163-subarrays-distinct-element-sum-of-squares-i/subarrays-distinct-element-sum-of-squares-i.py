class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        sum_squares = 0
       
        for start in range(len(nums)):
            seen = {}
            distinct_count = 0
            for end in range(start, len(nums)):
                # check current elements in hash map
                if nums[end] in seen:
                    seen[nums[end]] += 1
                else:  
                    seen[nums[end]] = 1
                    distinct_count += 1
            
                sum_squares += distinct_count ** 2
        return sum_squares

    
    ''' 
    start = 0:
    end = 0: [1] → distinct_count = 1 → sum_squares = 1
    end = 1: [1, 2] → distinct_count = 2 → sum_squares = 5
    end = 2: [1, 2, 1] → distinct_count = 2 → sum_squares = 9
    
    start = 1:
    end = 1: [2] → distinct_count = 1 → sum_squares = 10
    end = 2: [2, 1] → distinct_count = 2 → sum_squares = 14
    
    start = 2:
    end = 2: [1] → distinct_count = 1 → sum_squares = 15
    '''