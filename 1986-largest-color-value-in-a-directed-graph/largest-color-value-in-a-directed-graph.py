class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n

        for src, dst in edges:
            graph[src].append(dst)
            indegree[dst] += 1
        
        count = [[0] * 26 for _ in range(n)] #count[node][color] =  max number of times color c appeared on path to i
        
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
                count[i][ord(colors[i]) - ord('a')] = 1
        
        result = 0
        visited = 0

        while q:
            node = q.popleft()
            visited += 1
            for neighbor in graph[node]:
                for c in range(26):
                    # If color is same, then add 1
                    add = 1 if c == ord(colors[neighbor]) - ord('a') else 0
                    count[neighbor][c] = max(count[neighbor][c], count[node][c] + add)
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
            result = max(result, max(count[node]))

        return result if visited == n else -1