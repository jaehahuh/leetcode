class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for a, b in invocations:
            graph[a].append(b)
        
        sus = set([k])
        q = deque([k])

        while q:
            curr = q.popleft()
            for nxt in graph[curr]:
                if nxt not in sus:
                    sus.add(nxt)
                    q.append(nxt)
            
        for a, b in invocations:
            if a not in sus and b in sus:
                return list(range(n))
        
        return [i for i in range(n) if i not in sus]