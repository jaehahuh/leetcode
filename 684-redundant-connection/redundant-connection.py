class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #Union Find
        n = len(edges)
        parent = [i for i in range(n + 1)]  # parent[i] = i (self-parenting initially)
        rank = [1] * (n + 1)  # Initial rank of all nodes is 1
        
        #Finds the root parent of a node with path compressio
        def find(node):
            if node!= parent[node]:
                parent[node] = find(parent[node])
            return parent[node]

        #Unites two nodes into the same set, returns False if they already share a parent (cycle detected)
        def union(n1, n2):
            parent1, parent2 = find(node1), find(node2)
            # If both nodes have the same parent, a cycle is detected
            if parent1 == parent2:
                return False
            
            # Union by rank: attach the smaller tree to the larger one
            if rank[parent1] > rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2] # Update tree size
            else:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]

            return True
        
        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]