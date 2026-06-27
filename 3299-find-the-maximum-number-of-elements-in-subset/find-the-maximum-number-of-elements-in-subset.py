class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_len = 0

        # Subset consisting of only '1'
        if 1 in count:
            one_count = count[1]
            max_len = one_count - 1 if one_count % 2 == 0 else one_count
        
        for x in count:
            if x == 1:
                continue
            
            curr_len = 0
            curr_x = x

            while count[curr_x] >= 2 and curr_x ** 2 in count:
                curr_len += 2
                curr_x = curr_x ** 2
            
            curr_len += 1
            max_len = max(max_len, curr_len)
    
        return max_len