class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # Initialize the parent of each node. Each node is its own parent initially
        self.size = [1] * n  # Initialize the size of each node. Initially, all nodes have size 1
        self.edge_count = [0] * n  # Initialize the edge count for each component. All start at 0
    
    # Find the root of x
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        # If the roots are different, connect them
        if root_x != root_y:
            # Attach the smaller tree under the larger tree
            if self.size[root_x] < self.size[root_y]:
                self.parent[root_x] = root_y
                self.size[root_y] += self.size[root_x]
                self.edge_count[root_y] += self.edge_count[root_x]
                return root_y
            else:
                self.parent[root_y] = root_x
                self.size[root_x] += self.size[root_y]
                self.edge_count[root_x] += self.edge_count[root_y]
                return root_x
        return root_x

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for a, b in edges:
            uf.union(a,b) # Connect nodes a and b
            uf.edge_count[uf.find(a)] += 1
            uf.edge_count[uf.find(b)] += 1
        
        complete_components = 0
        seen = set() # Track already checked roots

        # Check the number of vertices and edges for each component
        for i in  range(n):
            root = uf.find(i)
            if root not in seen: # If this root hasn't been checked yet
                seen.add(root)
                vertices_count = uf.size[root] # Get the number of vertices in this component
                edges_count = uf.edge_count[root] // 2 # Divide by 2 since each edge is counted twice
                
                # Check the complete connection condition
                if edges_count == (vertices_count * (vertices_count - 1)) // 2:
                    complete_components += 1

        return complete_components 