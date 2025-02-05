class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build the graph
        graph = defaultdict(list)
        for i in range(len(times)):
            u, v, w = times[i] #source, target, time 
            graph[u].append((v, w))

        # Initialize the priority queue 
        q = [(0, k)] # (time, node) k = staring point
        visited = set()
        max_time = 0

        while q:
            current_time, current_node = heapq.heappop(q)
            if current_node in visited:
                continue
            visited.add(current_node)
            max_time = max(max_time, current_time)
            
            # Explore adjacent nodes
            for neighbor_node, travel_time in graph[current_node]:
                if neighbor_node not in visited:
                    heapq.heappush(q, (current_time + travel_time, neighbor_node))
        
        # Check if all nodes have been visited
        return max_time if len(visited) == n else -1