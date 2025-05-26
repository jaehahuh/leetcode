class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
        
        # Return max freq of color
        def dfs(node):
            if node in path:
                return float("inf") #Cycle
            if node in visited:
                return 0
        
            visited.add(node)
            path.add(node)
            
            color_index = ord(colors[node]) - ord('a')
            count[node][color_index] = 1

            for neighbor in graph[node]:
                if dfs(neighbor) == float('inf'):
                    return float("inf")
                for c in range(26):
                    count[node][c] = max(count[node][c], (1 if c == color_index else 0) + count[neighbor][c])
            
            path.remove(node)
            return max(count[node])

        result = 0
        visited = set()
        path = set()
        count = [[0] * 26 for _ in range(n)] #count[node][color] =  max number of times color c appeared on path to i
        for i in range(n): 
            result = max(result, dfs(i))

        return -1 if result == float("inf") else result