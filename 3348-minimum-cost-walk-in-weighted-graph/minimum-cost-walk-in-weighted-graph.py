class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n # Initialize the size of each node to 1
    
    # Function to find the root node of x
    def find(self, x):
        if x != self.parent[x]:
            # Set parent directly to root
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]
    
    # Function to connect x and y
    def union(self, x, y):
        x = self.find(x) # Find the root of x
        y = self.find(y) # Find the root of y
        # Only connect if they have different roots
        if x != y: 
            # Connect the smaller tree to the larger tree
            if self.size[x] < self.size[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        
        #1. Build Components
        uf = UnionFind(n)
        for u, v, w in edges:
            uf.union(u, v) # Connect nodes through each edge
        
        #2. Get cost of each component
        component_cost = {}  # root -> cost
        for u, v, w in edges:
            root = uf.find(u) # Find the root of u
            if root not in component_cost:
                component_cost[root] = w 
            else:
                # Update cost using bitwise AND if the root already exists
                component_cost[root] &= w
        
        #3. Queries
        result = []
        for src, dst in query:
            root1, root2 = uf.find(src), uf.find(dst)
            if root1 != root2: # If they are not connected
                result.append(-1) 
            else:
                result.append(component_cost[root1])

        return result