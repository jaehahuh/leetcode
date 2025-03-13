class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        result = -1
        left, right = 0, len(queries) # Initialize binary search bounds

        while left <= right:
            mid = (left + right) // 2
            decrement_array = [0] * (len(nums) + 1)  # Create an array to track decrements for nums


            for i in range(mid): # Loop through the queries from index 0 to mid - 1
                start, end, val = queries[i]
                decrement_array[start] += val
                if end + 1 < len(nums): # Check if the end index + 1 is within bounds
                    decrement_array[end + 1] -= val

            current_decrement = 0 
            can_make_zero = True  #Flag to check if zero array is possible
            
            # Check if the nums array can be made zero with the current decrements
            for i in range(len(nums)):
                current_decrement += decrement_array[i]
                if nums[i] > current_decrement:
                    can_make_zero = False
                    break

            if can_make_zero:
                result = mid
                right = mid - 1 # Search in the left half for a smaller k
            else:
                left = mid + 1 # Search in the right half for a larger k

        return result