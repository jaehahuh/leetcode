class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def bfs(row, col):
            q = deque([(row, col)])
            grid[row][col] = 1

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        q.append((nr,nc))
            
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and grid[r][c] == 0:
                    bfs(r,c)
        
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    islands += 1
                    bfs(r,c)
        
        return islands