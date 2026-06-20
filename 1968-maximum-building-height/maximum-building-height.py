class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        if not restrictions:
            return n - 1

        restrictions.append([1, 0])
        restrictions.append([n, n - 1])
        restrictions.sort()
        m = len(restrictions)

        for i in range(1, m):
            id1, h1 = restrictions[i-1]
            id2, h2 = restrictions[i]
            restrictions[i][1] = min(h2, h1 + (id2 - id1))
        
        
        for i in range(m-2, -1, -1):
            id1, h1 = restrictions[i]
            id2, h2 = restrictions[i+1]
            restrictions[i][1] = min(h1, h2 + (id2 - id1))
        
        result = 0
        for i in range(1, m):
            id1, h1 = restrictions[i - 1]
            id2, h2 = restrictions[i]
            dist = id2 - id1
            
            max_val = (h1 + h2 + dist) // 2
            result = max(result, max_val)
            
        return result