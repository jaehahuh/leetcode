class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b, dist in roads:
            graph[a].append((b,dist))
            graph[b].append((a,dist))
        
        q = deque([1])
        visited = set([1])
        min_dist = float('inf')

        while q:
            curr_city = q.popleft()
            for neighbor, dist in graph[curr_city]:
                min_dist = min(min_dist, dist)
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        
        return min_dist