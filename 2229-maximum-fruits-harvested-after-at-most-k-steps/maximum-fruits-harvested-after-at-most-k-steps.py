class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        positions = [fruit[0] for fruit in fruits]
        amounts = [fruit[1] for fruit in fruits]
        n = len(fruits)
        
        # Calculate prefix sums for fruit amounts
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + amounts[i]
        
        max_fruits = 0
        left = 0 
        
        for right in range(n): 
            # Adjust the left pointer to ensure the window is valid given 'k' steps
            while left <= right: 
                left_pos = fruits[left][0]
                right_pos = fruits[right][0]

                cost = 0
                # Case 1: startPos is to the left of or at the leftmost fruit in the window
                if startPos <= left_pos: 
                    cost = right_pos - startPos
                # Case 2: startPos is to the right of or at the rightmost fruit in the window
                elif startPos >= right_pos:
                    cost = startPos - left_pos
                # Case 3: startPos is inside the window (left_pos < startPos < right_pos)
                else: 
                    # Option 1: Go left first (startPos -> left_pos -> right_pos)
                    cost1 = (startPos - left_pos) + (right_pos - left_pos)
                    # Option 2: Go right first (startPos -> right_pos -> left_pos)
                    cost2 = (right_pos - startPos) + (right_pos - left_pos)
                    cost = min(cost1, cost2)

                # If the cost to cover the current window [left_pos, right_pos] is within k steps
                if cost <= k:
                    # Calculate the total fruits in the current window using prefix sums
                    curr_fruits = prefix_sum[right + 1] - prefix_sum[left]
                    # Update the maximum fruits harvested so far
                    max_fruits = max(max_fruits, curr_fruits)
                    # Break the inner while loop as this 'left' is valid, and moving it further right
                    # would only shrink the window, not improve the result for this 'right'.
                    break 
                else:
                    # If the cost exceeds k, shrink the window from the left
                    # by moving the left pointer to the right.
                    left += 1
            
        # Return the maximum fruits harvested after checking all valid windows
        return max_fruits