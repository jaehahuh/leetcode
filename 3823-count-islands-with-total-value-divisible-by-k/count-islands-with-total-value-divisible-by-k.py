class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        def bfs(row, col):
            q = deque([(row, col)])
            total_value = grid[row][col]
            grid[row][col] = 0
            directions = [(1,0), (-1,0), (0, 1), (0, -1)]
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc= r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 0:
                        total_value += grid[nr][nc]
                        grid[nr][nc] = 0
                        q.append((nr, nc))
                
            return total_value
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    island_sum = bfs(r, c)
                    if island_sum % k == 0:
                        count += 1
        
        return count
