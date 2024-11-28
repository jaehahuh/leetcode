class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])  #m:row, n:column (numbers of elements in row)
        direction = [(-1,0), (1,0), (0,-1), (0, 1)]
        min_heap = [(0, 0, 0)] #(cost, x, y)
        visited = [[False] * n for _ in range(m)] 
        
        while min_heap:
            cost, x, y = heapq.heappop(min_heap)
            # reached bottom-right corner
            if x == m - 1 and y == n - 1: 
                return cost
            
            if visited[x][y]: #if visited[x][y] is True, then move to next cell
                continue

            visited[x][y] = True

            for x_dir, y_dir in direction:
                dx = x + x_dir
                dy = y + y_dir
                if 0 <= dx < m  and 0 <= dy < n and not visited[dx][dy]:
                    # Add to heap(min_heap) with updated cost
                    heapq.heappush(min_heap, (cost+grid[dx][dy], dx, dy))