class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        # right_inc[i]: Max length of a strictly increasing subarray starting at nums[i]
        right_inc = [0] * n
        right_inc[-1] = 1

        for i in range(n-2, -1, -1):
            if nums[i] < nums[i + 1]:
                right_inc[i] = right_inc[i + 1] + 1
            else:
                right_inc[i] = 1
        
        # Helper function to check if a given k satisfies the problem conditions
        def check(k) -> bool:
            if k == 0 or 2*k > n:
                return False
            
            for i in range(n - 2 * k + 1):
                # Check if both adjacent subarrays (starting at i and i+k) are strictly increasing
                if right_inc[i] >= k and right_inc[i + k] >= k:
                    return True # Found a valid k
            return False # No valid 'i' found for this k

        left = 1
        right = n//2
        result = 0

        while left <= right:
            mid = left + (right-left)//2
            if check(mid):
                result = mid
                left = mid + 1 # Try to find a larger k
            else:
                right = mid - 1 # mid is not possible, try smaller k

        return result