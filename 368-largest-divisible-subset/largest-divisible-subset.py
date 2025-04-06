class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        # dp[i] stores the maximum length of the divisible subset that ends with nums[i]
        dp = [1] * n   

        # prev[i] stores the index of the previous element in the subset that ends with nums[i]       
        prev = [-1] * n       # -1 indicates that there is no previous element

        # Track the index of the last element of the largest divisible subset
        max_subset_index = 0     

        # Build the dp and prev arrays by checking divisibility for every pair 
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > dp[max_subset_index]:
                max_subset_index = i

        # Reconstruct the largest divisible subset by backtracking through the prev array
        largest_subset = []
        while max_subset_index != -1:
            largest_subset.append(nums[max_subset_index])
            max_subset_index = prev[max_subset_index]

        return largest_subset[::-1]  # The subset is built in reverse order, so reverse it before returning