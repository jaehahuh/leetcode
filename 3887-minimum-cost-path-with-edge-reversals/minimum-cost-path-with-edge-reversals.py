class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w, 0))
            adj[v].append((u, w, 1))

        dist = [[float('inf')] * 2 for _ in range(n)]

        min_heap = [(0, 0, 0)]
        dist[0][0] = 0

        while min_heap:
            current_cost, u, switch_available = heapq.heappop(min_heap)

            if current_cost > dist[u][switch_available]:
                continue

            for v, weight, edge_type in adj[u]:
                new_cost = current_cost
                
                if edge_type == 0:
                    new_cost += weight
                    if new_cost < dist[v][0]:
                        dist[v][0] = new_cost
                        heapq.heappush(min_heap, (new_cost, v, 0))
                else:
                    if switch_available == 0:
                        new_cost += 2 * weight
                        if new_cost < dist[v][0]:
                            dist[v][0] = new_cost
                            heapq.heappush(min_heap, (new_cost, v, 0))

        result = min(dist[n-1][0], dist[n-1][1])
        return result if result != float('inf') else -1