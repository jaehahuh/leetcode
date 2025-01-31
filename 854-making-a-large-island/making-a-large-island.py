class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Check if the given coordinates are out of grid bounds
        def is_out_of_bounds(r, c):
            return r < 0 or c < 0 or r >= n or c >= n
        
        # DFS to explore an island and return its size
        def dfs(r, c, label):
            if is_out_of_bounds(r, c) or grid[r][c] != 1:
                return 0
            grid[r][c] = label  # Mark the current position with a label
            size = 1
            for dr, dc in directions:
                size += dfs(r + dr, c + dc, label) 
            
            return size

        # 1. Label all islands and store their sizes
        island_sizes = {}  # {label: size}
        label = 2  # Start labeling from 2 to distinguish from 1
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    island_sizes[label] = dfs(r, c, label)  # Store island size
                    label += 1  # Increment label for the next island

        # Calculate the maximum island size if a 0 at (r, c) is flipped to 1
        def get_connected_size(r, c):
           
            visited_labels = set()
            total_size = 1  # Start with size 1 since we flip one 0 to 1
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not is_out_of_bounds(nr, nc) and grid[nr][nc] > 1:
                    label = grid[nr][nc]
                    if label not in visited_labels:  # Avoid counting the same island multiple times
                        total_size += island_sizes[label]
                        visited_labels.add(label)

            return total_size

        # 2. Flipping each 0 to 1 and find the largest island possible
        max_size = max(island_sizes.values(), default=0)  # Max size of existing islands
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    max_size = max(max_size, get_connected_size(r, c))

        return max_size