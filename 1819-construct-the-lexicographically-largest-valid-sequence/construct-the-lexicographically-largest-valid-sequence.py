class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        # Initialize the result list
        result = [0] * (2 * n - 1)
        used = set()  # Track numbers that have already been placed

        def backtracking(index):
            # If all indices are filled, return success
            if index == len(result):
                return True
            
            # Try numbers from largest to smallest
            for num in reversed(range(1, n + 1)):
                # Skip if the number is already used or if the distance condition fails
                if num in used:
                    continue
                if num > 1 and (index + num >= len(result) or result[index + num] != 0):
                    continue
                # Place the number
                used.add(num)
                result[index] = num
                if num > 1:
                    result[index + num] = num
                
                # Find the next empty position
                next_index = index + 1
                while next_index < len(result) and result[next_index] != 0:
                    next_index += 1
            
                # Recursive call
                if backtracking(next_index):
                    return True  # Exit on success
                
                # Backtrack: if the current path is not valid, undo the choice
                used.remove(num) # Remove the number from the used set
                result[index] = 0 # Reset the current index
                if num > 1:
                    result[index + num] = 0  # Reset the second occurrence position
                     
            return False  # Failed after trying all numbers
        
        backtracking(0)
        return result