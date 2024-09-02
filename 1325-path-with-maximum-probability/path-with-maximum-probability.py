class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i] #unpacking edges list
            adj[src].append([dst, succProb[i]])
            adj[dst].append([src, succProb[i]])
        
        priority_q = [(-1, start_node)] #start probability with 1
        visit = set()
        
        while priority_q:
            prob, cur = heapq.heappop(priority_q)
            visit.add(cur)

            if cur == end_node:
                return prob * -1
            
            for neighbor, edgeProb in adj[cur]:
                if neighbor not in visit:
                    heapq.heappush(priority_q, (prob * edgeProb, neighbor))
        return 0