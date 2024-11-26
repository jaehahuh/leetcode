class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        incoming_edges = [0] * n
        for src, dst in edges:
            incoming_edges[dst] += 1
    
        champions = []
        for i, incoming_count in enumerate(incoming_edges):
            if incoming_count == 0: 
                champions.append(i)
        
        if len(champions) != 1: #if number of champion is greater than one or None, return -1 
            return -1
        
        return champions[0]