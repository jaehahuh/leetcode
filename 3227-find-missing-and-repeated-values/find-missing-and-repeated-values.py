class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        # Create a dictionary with keys from 1 to n^2, initializing each count to 2
        count_dict = {num:2 for num in range(1, n**2 + 1)}

        for i in range(n):
            for j in range(n):
                count_dict[grid[i][j]] -= 1

        # Determine the repeated and missing numbers based on the counts
        for key, count in count_dict.items():
            if count == 0 :
                repeated = key
            if count == 2 :
                missing = key
        
        return [repeated, missing]