class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # Precompute sums of subarrays of length k
        k_sums = [sum(nums[:k])] 
        for i in range(k, len(nums)):
            k_sums.append(k_sums[-1] + nums[i] - nums[i-k])
       
        dp = {}  # Cache

        # Helper function to calculate max sum recursively
        def get_max_sum(i, count):
            # Base case: all 3 subarrays chosen or out of bounds
            if count == 3 or i > len(nums) - k:
                return 0
            if (i,count) in dp: # Check memoization cache
                return dp[(i, count)]
            
            # Option 1: Include the current subarray
            include = k_sums[i] + get_max_sum(i + k, count + 1)
            # Option 2: Skip the current subarray
            skip = get_max_sum(i+1, count)

            # Store and return the maximum of include or skip
            dp[(i, count)] = max(include, skip)
            return dp[(i, count)]
        
        # Reconstruct the indices of the chosen subarrays
        def get_indices():
            i = 0
            indices = []
            while i <=  len(nums) - k and len(indices) < 3:
                include = k_sums[i] + get_max_sum(i + k, len(indices) + 1)
                skip = get_max_sum(i + 1, len(indices))

                if include >= skip: # If including gives a better result, choose this index
                    indices.append(i)
                    i += k  # Move forward by k to avoid overlap
                else:
                    i += 1 # Otherwise, move to the next index
            return indices

        return get_indices() 