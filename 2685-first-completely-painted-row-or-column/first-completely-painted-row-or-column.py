class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows, columns = len(mat), len(mat[0])
        # Create a hashmap to store the position of each number
        hash_map = {} # n = (r, c)
        for r in range(rows):
            for c in range(columns):
                hash_map[mat[r][c]] = (r, c) 

        # Initialize counters for painted cells in each row and column
        row_count = [0] * rows
        col_count = [0] * columns

        # Traverse through arr and paint the corresponding cells in the matrix
        for i in range(len(arr)):
            r, c = hash_map[arr[i]]
            row_count[r] += 1
            col_count[c] += 1

            # Check if a row or column is fully painted
            if col_count[c] == rows or row_count[r] == columns:
                return i