class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        component_count = [0]
        def dfs(current, parent):
            total = values[current]
            for child in graph[current]:
                if child != parent:
                    total += dfs(child, current)
            # divisible with K
            if total % k == 0:
                component_count[0] += 1
            return total
    
        # DFS start
        dfs(0, -1)

        return component_count[0]