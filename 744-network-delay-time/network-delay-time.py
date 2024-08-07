class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #build the graph as an adjacency list
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w)) 

        #initialize distances and the priority queue
        distances = {}
        for i in range(1, n+1):
            distances[i] = float('inf')
        distances[k] = 0
        priority_queue = [(0, k)]

        #implement Dijkstra's Algorithm
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
        
            if current_distance > distances[current_node]:
                continue
            
            for v, w in graph[current_node]:
                dist = current_distance + w
                if dist < distances[v]:
                    distances[v] = dist
                    heapq.heappush(priority_queue, (dist, v))
        
        #determine the existence of shortest paths for all paths
        max_distance = max(distances.values())
        if max_distance < float('inf'): 
            return max_distance
        else:
            return -1