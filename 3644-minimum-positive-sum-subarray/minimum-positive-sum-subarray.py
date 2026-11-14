class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float('inf')
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        for length in range(l, r + 1):
            for i in range(n - length + 1):
                curr_sum = prefix[i + length] - prefix[i]
                if 0 < curr_sum < min_sum:
                    min_sum = curr_sum
                    
        return min_sum if min_sum != float('inf') else -1