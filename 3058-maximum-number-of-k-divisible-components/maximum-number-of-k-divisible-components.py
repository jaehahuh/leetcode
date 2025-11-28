class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        num_components = 0
        def dfs(curr, parent):
            nonlocal num_components
            total = values[curr]
            for child in graph[curr]:
                if child != parent:
                    total += dfs(child, curr)
            
            if total % k == 0:
                num_components += 1
            return total
        
        dfs(0, -1)
        return num_components