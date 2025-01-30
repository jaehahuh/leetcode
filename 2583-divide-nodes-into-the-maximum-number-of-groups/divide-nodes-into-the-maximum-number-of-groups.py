class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # Create an adjacency list for the graph
        graph = defaultdict(list)
        # Undirected graph
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        # BFS to find the connected component containing the start node
        def get_connected_component(start):
            q = deque([start])
            component = set([start])
            visited.add(start)

            while q:   
                node = q.popleft()
                for neighbor in graph[node]:
                    if neighbor not in component:
                        q.append(neighbor)
                        component.add(neighbor)
                        visited.add(neighbor)
            return component
        
        # BFS to find the maximum group count (depth) in a componen
        def bfs_max_depth(start):
            q = deque([(start, 1)]) #(node, group)
            level_map = {start:1}
            max_depth = 1

            while q:
                node, level = q.popleft()
                max_depth = max(max_depth, level)

                for neighbor in graph[node]:
                    if neighbor in level_map:
                        if abs(level_map[neighbor] - level) != 1:
                            return - 1 # Not a bipartite graph
                        continue
                    q.append((neighbor, level + 1))
                    level_map[neighbor] = level + 1
            return max_depth


        visited = set()
        total_groups = 0

        for node in range(1, n + 1):
            if node in visited:
                continue    
            component = get_connected_component(node)  # Get all nodes in the component
            max_component_depth = 0

            for start in component:
                depth = bfs_max_depth(start) # Find max depth from any node
                if depth == -1:
                    return -1
                max_component_depth = max(max_component_depth, depth)

            total_groups += max_component_depth  # Add max depth of each component
        return total_groups