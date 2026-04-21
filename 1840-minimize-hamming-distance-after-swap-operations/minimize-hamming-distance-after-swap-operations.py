class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        graph = defaultdict(list)
        for a, b in allowedSwaps:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * n

        def dfs(node, group):
            visited[node] = True
            group.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, group)
        
        result = 0
        
        for i in range(n):
            if not visited[i]:
                group = []
                dfs(i, group)

                source_count = Counter(source[i] for i in group)
                target_count = Counter(target[i] for i in group)

                diff = source_count - target_count
                result += sum(diff.values())
            
        return result