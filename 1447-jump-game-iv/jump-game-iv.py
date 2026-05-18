class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        
        # 같은 값을 가진 인덱스들을 그룹화
        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
            
        # BFS를 위한 큐와 방문 여부 체크 배열 (index, steps)
        queue = deque([(0, 0)])
        visited = {0}
        
        while queue:
            curr_idx, steps = queue.popleft()
            
            if curr_idx == n - 1:
                return steps
            
            next_indices = []
            
            if curr_idx + 1 < n:
                next_indices.append(curr_idx + 1)
            if curr_idx - 1 >= 0:
                next_indices.append(curr_idx - 1)
            if arr[curr_idx] in graph:
                next_indices.extend(graph[arr[curr_idx]])
                del graph[arr[curr_idx]]
                
            for nxt in next_indices:
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))
                    
        return -1