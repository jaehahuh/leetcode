class Solution:
    def minOperations(self, nums: List[int]) -> int:
        op = float('inf')
        n = len(nums)

        if n == 1:
            return 0
        
        zero_index = nums.index(0)

        def check(step) -> bool:
            for i in range(1, n):
                prev = (zero_index + (i-1) * step) % n
                curr = (zero_index + i * step) % n
                if nums[prev] > nums[curr]:
                    return False
            return True
        
        if check(1): 
            op = min(op, zero_index)  # only rotate
            op = min(op, n - zero_index + 2) # rotate -> reverse -> rotate
        
        if check(-1):
            op = min(op, zero_index + 2) # rotate -> reverse
            op = min(op, n - zero_index) # reverse -> rotate

        return op if op != float('inf') else -1