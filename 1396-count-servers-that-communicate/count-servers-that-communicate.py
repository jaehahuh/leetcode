class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        server = 0 # Count of servers that can communicate
        rows = len(grid)
        columns = len(grid[0])

        # Lists to store the count of servers in each row and column
        row_count = [0] * rows
        col_count = [0] * columns

        # Preprocessing: Count the number of servers in each row and column
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    row_count[r] += 1
                    col_count[c] += 1

        # Check each server's position to see if it can communicate
        for r in range(rows):
            for c in range(columns):
                # If there is a server at this position, and there is more than one server
                # in either the same row or the same column
                if grid[r][c] and (row_count[r] > 1 or col_count[c] > 1):
                    server += 1  # Count this server as able to communicate

        return server