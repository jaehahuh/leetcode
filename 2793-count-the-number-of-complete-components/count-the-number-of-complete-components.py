class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        complete_count = 0

        for i in range(n):
            if not visited[i]:
                q = deque([i])
                visited[i] = True

                vertex_count = 0
                edge_count = 0

                while q:
                    node = q.popleft()
                    vertex_count += 1
                    edge_count += len(graph[node])

                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            q.append(neighbor)
                    
                if edge_count == vertex_count * (vertex_count - 1):
                    complete_count += 1

        return complete_count