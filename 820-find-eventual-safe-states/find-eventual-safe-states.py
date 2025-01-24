class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = [False] * n
        visited = [0] * n  # 0: unvisited, 1: visiting, 2: visited

        def dfs(node):
            if visited[node] != 0:
                return visited[node] == 2
            visited[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            visited[node] = 2
            return True

        for i in range(n):
            dfs(i)

        return [i for i in range(n) if visited[i] == 2]