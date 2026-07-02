class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        min_cost = [[float('inf')] * n for _ in range(m)] 
        min_cost[0][0] = grid[0][0]
        q = deque([(0,0)])

        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while q:
            r, c = q.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = min_cost[r][c] + grid[nr][nc]

                    if new_cost < min_cost[nr][nc]:
                        min_cost[nr][nc] = new_cost

                        if grid[nr][nc] == 0:
                            q.appendleft((nr,nc))
                        else:
                            q.append((nr,nc))

        return min_cost[m-1][n-1] < health