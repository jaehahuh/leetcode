class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def build_tree(edges):
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            return graph

        def bfs(tree, n):
            depth = [0] * n
            visited = [False] * n
            q = deque()
            q.append(0)
            visited[0] = True

            while q:
                node = q.popleft()
                for neighbor in tree[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        depth[neighbor] = depth[node] + 1
                        q.append(neighbor)
            
            parity = [d % 2 for d in depth]
            count = [0, 0]

            for p in parity:
                count[p] += 1
            
            return parity, count

        n = len(edges1) + 1
        m = len(edges2) + 1
        tree1 = build_tree(edges1)
        tree2 = build_tree(edges2)

        parity1, count1 = bfs(tree1, n)
        _, count2 = bfs(tree2, m)

        max_count2 = max(count2)
        result = []
        for p in parity1:
            result.append(count1[p] + max_count2)
        return result