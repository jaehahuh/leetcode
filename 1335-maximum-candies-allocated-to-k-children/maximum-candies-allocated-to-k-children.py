class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # Return 0 if the total number of candies is less than the number of children
        total_candies = sum(candies)
        if total_candies < k:
            return 0

        # Initialize the range for binary search
        left, right = 1, total_candies // k
        max_candies_per_child = 0

        while left <= right:
            mid = (left + right) // 2
            count = 0
            
            # Calculate how many pieces of mid size can be obtained from each candy pile
            for candy in candies:
                count += candy // mid
            
            # Check if we can distribute at least k pieces
            if count >= k:
                max_candies_per_child = mid  # Update the maximum candies per child
                left = mid + 1  # Try for more candies
            else:
                right = mid - 1  # Try with fewer candies
        
        return max_candies_per_child