class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0] * (n+1)

    def find(self, x):
        # path compression iterative
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        else:
            self.parent[rb] = ra
            if self.rank[ra] == self.rank[rb]:
                self.rank[ra] += 1

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        dsu = DSU(c)
        for u, v in connections:
            dsu.union(u, v)

        comp_heaps = {}  # root -> heap(list)
        for v in range(1, c+1):
            r = dsu.find(v)
            if r not in comp_heaps:
                comp_heaps[r] = []
            comp_heaps[r].append(v)
        for r in comp_heaps:
            heapq.heapify(comp_heaps[r])


        live = [True] * (c+1)  # 1-based

        result = []
        for typ, x in queries:
            if typ == 2:
                # offline
                live[x] = False
            else:  # typ == 1
                if live[x]:
                    result.append(x)
                else:
                    r = dsu.find(x)
                    if r not in comp_heaps:
                        result.append(-1)
                        continue
                    h = comp_heaps[r]
                    while h and not live[h[0]]:
                        heapq.heappop(h)
                    if h:
                        result.append(h[0])
                    else:
                        result.append(-1)
        return result
