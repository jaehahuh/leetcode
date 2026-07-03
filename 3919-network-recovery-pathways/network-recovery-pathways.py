class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        graph = [[] for _ in range(n)]
        max_cost = 0
        
        for u, v, cost in edges:
            graph[u].append((v, cost))
            if cost > max_cost:
                max_cost = cost
        
        def check(mid: int) -> int:
            memo = {}
            
            def dfs(u: int) -> int:
                if u == n - 1:
                    return 0
                if u in memo:
                    return memo[u]
                
                min_cost = float('inf')
                
                for v, cost in graph[u]:
                    if not online[v] or cost < mid:
                        continue
                    
                    path_cost = dfs(v)
                    if path_cost != float('inf'):
                        min_cost = min(min_cost, cost + path_cost)
                        
                memo[u] = min_cost
                return min_cost
            
            return dfs(0)

        if check(0) > k:
            return -1
            
        left = 0
        right = max_cost
        ans = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if check(mid) <= k:
                ans = mid        
                left = mid + 1   
            else:
                right = mid - 1
                
        return ans