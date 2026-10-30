class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        dist = [[math.inf] * (k + 1) for _ in range(n)]
        
        pq = []
        
        heapq.heappush(pq, (0, 0, 1))
        dist[0][1] = 0
        
        while pq:
            w, u, c = heapq.heappop(pq)
            
            if w > dist[u][c]:
                continue
                
            if u == n - 1:
                return w

            for v, weight in adj[u]:
                if labels[u] == labels[v]:
                    nc = c + 1
                else:
                    nc = 1
                
                if nc <= k:
                    if w + weight < dist[v][nc]:
                        dist[v][nc] = w + weight
                        heapq.heappush(pq, (w + weight, v, nc))
                        
        return -1