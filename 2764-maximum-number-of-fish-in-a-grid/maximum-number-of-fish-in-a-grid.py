class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            # If out of bounds, cell is land (0), or already visited, terminate the search
            if (r < 0 or c < 0 or r == rows or c == columns or grid[r][c] == 0 or (r, c) in visited):
                return 0
            visited.add((r, c))
            current_fishes = grid[r][c]
            directions = [(0,-1), (0,1), (-1,0), (1,0)] #(left, right, down, up)
            for dr, dc in directions:
                # Perform DFS for each adjacent cell
                current_fishes += dfs(r + dr, c + dc)
            return current_fishes

        result = 0
        visited = set()  # Set to track visited cells
        rows, columns = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(columns):
                # If the current cell contains fish and is not yet visited, start DFS
                if grid[r][c] > 0 and (r, c) not in visited:
                    # Update the maximum number of fish found
                    result = max(result, dfs(r, c))
        return result