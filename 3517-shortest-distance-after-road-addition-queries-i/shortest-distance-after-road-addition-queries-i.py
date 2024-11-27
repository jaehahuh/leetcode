from collections import defaultdict, deque
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        # initialize path (0 -> 1 -> 2 -> ... -> n-1)
        for i in range(n - 1):
            graph[i].append(i + 1)
        
        def bfs():
            queue = deque()
            queue.append((0,0)) #(current node, length)
            visited = set()
            visited.add((0)) # check visited node
            while queue:
                cur_node, length = queue.popleft()
                if cur_node == n - 1:
                    return length
                for neighbor in graph[cur_node]:
                    if neighbor not in visited:
                        queue.append((neighbor, length + 1))
                        visited.add(neighbor)
                             
        result = []
        for src, dst in queries:
            graph[src].append(dst) #add new path
            result.append(bfs()) # calculate shortest path
        return result