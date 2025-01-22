class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows = len(isWater)
        columns = len(isWater[0]) 
        q = deque() #(row, column)
        map_of_highest_peak = [[-1]*columns for _ in range(rows)] # Initialize: -1 indicates unvisited cells

        # Enqueue all water cells and set their height to 0
        for r in range(rows):
            for c in range(columns):
                if isWater[r][c] == 1:
                    q.append((r,c))
                    map_of_highest_peak[r][c] = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        #BFS 
        while q:
            r, c = q.popleft()
            height = map_of_highest_peak[r][c]
            # Move in four directions
            for d_row, d_col in directions:
                neighbor_row = r + d_row
                neighbor_col = c + d_col
                # Check bounds and if the neighbor is already visited
                if 0 <= neighbor_row < rows and 0 <= neighbor_col < columns and map_of_highest_peak[neighbor_row][neighbor_col] == -1:
                    q.append((neighbor_row, neighbor_col))
                    map_of_highest_peak[neighbor_row][neighbor_col] = height + 1

        return map_of_highest_peak