class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
    
        def dfs(x, y, from_x, from_y, char, length):
            if visited[x][y]:
                # 방문한 노드를 다시 만났을 때 길이가 4 이상이면 사이클 존재
                return length - 1 >= 4
            visited[x][y] = True
            
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == char:
                    if (nx, ny) == (from_x, from_y):
                        # 바로 이전 위치로는 이동 금지
                        continue
                    if dfs(nx, ny, x, y, char, length + 1):
                        return True
            return False
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1, grid[i][j], 1):
                        return True
        return False