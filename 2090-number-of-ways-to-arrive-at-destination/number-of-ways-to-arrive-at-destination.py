class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, t in roads:
            graph[u].append((t, v)) # (cost, destination node)
            graph[v].append((t, u)) # (cost, destination node)
        
        MOD = 10**9 + 7
        min_heap = [(0, 0)] # (current cost, current node)
        min_cost = [float('inf')] * n

        path_count = [0] * n # Initialize path count for each node
        path_count[0] = 1  # Path count to start node is 1

        # Dijkstra's algorithm 
        while min_heap:
            cost, node = heappop(min_heap) # Select the node with minimum cost
            for nei_cost, nei in graph[node]:
                new_cost = cost + nei_cost # Total cost to reach adjacent node

                # New shortest path found
                if new_cost < min_cost[nei]:
                    min_cost[nei] = new_cost # Update minimum cost
                    path_count[nei] = path_count[node]
                    heappush(min_heap, (new_cost, nei))

                # Same shortest path found
                elif new_cost == min_cost[nei]:
                    path_count[nei] = (path_count[nei] + path_count[node]) % MOD # Sum path counts

        return path_count[n-1]