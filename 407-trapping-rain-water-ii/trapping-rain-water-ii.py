from heapq import heappush, heappop

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0  #테두리만 있어서 물이 고이지 않음
        
        visited = [[False] * n for _ in range(m)]
        heap = []

        # 세로 테두리 힙에 삽입
        for r in range(m):
            for c in (0, n-1):
                heappush(heap, (heightMap[r][c], r, c))
                visited[r][c] = True
        
        # 가로 테두리 힙에 삽입
        for c in range(n):
            for r in (0, m-1):
                if not visited[r][c]:
                    heappush(heap, (heightMap[r][c], r, c))
                    visited[r][c] = True
        

        water = 0 # 현재까지의 물수위(가장 낮은 경계의 최대치)
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while heap:
            h, r, c = heappop(heap)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    nh = heightMap[nr][nc]
                    # 현재 경계 높이 h가 물수위 역할
                    if nh < h:
                        water += h - nh
                        # 물이 찼다면 유효 높이는 h로 상승
                        heappush(heap, (h, nr, nc))
                    else:
                        heappush(heap, (nh, nr, nc))
        return water