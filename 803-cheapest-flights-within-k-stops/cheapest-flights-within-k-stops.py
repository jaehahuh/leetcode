class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for from_city, to_city, price in flights:
            graph[from_city].append((to_city, price))
        
        # Initialize priority queue
        q = [(0, src, k)]  # (total cost, current city, remaining stops)

        # Cost tracking: visited[node][remaining_stops]
        visited = [[float('inf')] * (k + 2) for _ in range(n)]
        visited[src][k + 1] = 0

        while q:
            total_price, node, remaining_stops = heapq.heappop(q)
            if node == dst:
                return total_price
            if remaining_stops >= 0:
                for to_city, price in graph[node]:
                    new_price = total_price + price
                    # Only add to the queue if the new cost is cheaper
                    if new_price < visited[to_city][remaining_stops - 1]:
                        visited[to_city][remaining_stops - 1] = new_price
                        heapq.heappush(q, (new_price, to_city, remaining_stops - 1))

        return -1