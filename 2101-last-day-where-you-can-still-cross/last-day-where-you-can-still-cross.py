class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        result = 0
        low = 1
        high = len(cells)

        def bfs(day):
            grid = [[0] * col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                grid[r-1][c-1] = 1 
            
            visited = [[False] * col for _ in range(row)]
            
            q = collections.deque()
            for c_idx in range(col):
                if grid[0][c_idx] == 0: 
                    q.append((0, c_idx))
                    visited[0][c_idx] = True
            
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while q:
                r, c = q.popleft()
                if r == row - 1:
                    return True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                
               
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0 and not visited[nr][nc]:
                        visited[nr][nc] = True
                        q.append((nr, nc))
        
            return False
        
        while low <= high:
            mid = low + (high - low)//2

            if bfs(mid):
                result = mid
                low = mid + 1
            
            else:
                high = mid - 1
        
        return result