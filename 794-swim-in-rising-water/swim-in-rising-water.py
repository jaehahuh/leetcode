class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        min_heap = [(grid[0][0], 0, 0)] # min-heap: (path_max_elevation, r, c)
        visited = [[False] * n for _ in range(n)]

        direcs = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        while min_heap:
            # Pop the cell with the minimal path max elevation so far
            cost, r, c = heapq.heappop(min_heap) # cost = pax_max_elevation

            # Skip visited cell
            if visited[r][c]:
                continue
            
            visited[r][c] = True

            if r == n - 1 and c == n - 1:
                return cost  # Answer

            # Explore neighbors and push the resulting path cost
            for dr, dc in direcs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    #  Path cost to neighbor is max(neighbor elevation, current cost)
                    next_cost = max(grid[nr][nc], cost)
                    # Push into min-heap so smaller costs expand first
                    heapq.heappush(min_heap, (next_cost, nr, nc))