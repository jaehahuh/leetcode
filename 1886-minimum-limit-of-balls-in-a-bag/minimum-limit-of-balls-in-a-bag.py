class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        low, high = 1, max(nums)
        while low < high:
            mid = (low + high) // 2
            operations_needed = 0
    
            for balls in nums:
                operations_needed += (balls - 1) // mid
    
            if operations_needed > maxOperations:
                low = mid + 1
            else:
                high = mid
        
        return low