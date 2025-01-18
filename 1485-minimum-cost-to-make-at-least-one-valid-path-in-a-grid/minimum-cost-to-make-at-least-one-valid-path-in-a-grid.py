class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 오른쪽, 왼쪽, 아래, 위
        costs = [[float('inf')] * n for _ in range(m)]
        costs[0][0] = 0
        
        # 우선순위 큐를 사용하여 비용이 적은 순서로 탐색
        pq = [(0, 0, 0)]  # (비용, x좌표, y좌표)
        
        while pq:
            cost, x, y = heapq.heappop(pq)
            
            if (x, y) == (m - 1, n - 1):
                return cost
            
            if cost > costs[x][y]:
                continue
            
            for i in range(4):
                nx, ny = x + directions[i][0], y + directions[i][1]
                if 0 <= nx < m and 0 <= ny < n:
                    next_cost = cost + (1 if grid[x][y] != i + 1 else 0)  # 현재 방향과 일치하지 않으면 비용 추가
                    if next_cost < costs[nx][ny]:
                        costs[nx][ny] = next_cost
                        heapq.heappush(pq, (next_cost, nx, ny))
        
        return costs[m - 1][n - 1]