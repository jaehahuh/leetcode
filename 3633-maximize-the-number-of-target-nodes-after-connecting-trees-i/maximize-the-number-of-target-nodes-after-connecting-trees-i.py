class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def build_tree(edges, size):
            graph = [[] for _ in range(size)]
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            return graph

        #Calculate the number of reach nodes by distance for each node
        def bfs_count(graph, start, max_dist):
            visited = [False] * len(graph)
            dist = [0] * len(graph)
            queue = deque([start])
            visited[start] = True
            count = 0

            while queue:
                u = queue.popleft()
                if dist[u] > max_dist:
                    continue
                count += 1
                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        dist[v] = dist[u] + 1
                        queue.append(v)
            return count

        n = len(edges1) + 1
        m = len(edges2) + 1
        tree1 = build_tree(edges1, n)
        tree2 = build_tree(edges2, m)
        
        tree2_reach = [bfs_count(tree2, i, k - 1) for i in range(m)]

        result = []
        for i in range(n):
            count1 = bfs_count(tree1, i, k)
            max_total = 0
            for j in range(m):
                max_total = max(max_total, count1 + tree2_reach[j])
            result.append(max_total)

        return result