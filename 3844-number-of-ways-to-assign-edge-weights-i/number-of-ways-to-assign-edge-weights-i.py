class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(edges) + 1

        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        max_depth = 0
        q = deque([(1, 0)]) # (현재 노드, 현재까지의 간선 개수)
        visited = [False] * (n + 1)
        visited[1] = True

        while q:
            curr, depth = q.popleft()
            max_depth = max(max_depth, depth)

            for neighbor in adj[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append((neighbor, depth + 1))
        
        result = pow(2, max_depth -1, MOD)
        return result