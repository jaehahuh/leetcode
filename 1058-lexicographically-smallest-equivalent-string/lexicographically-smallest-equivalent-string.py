class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        #Union Find
        #Initialize Union-Find parent array for 26 lowercase letters (0 for 'a', 1 for 'b', ..., 25 for 'z')
        parent = list(range(26))
        
        # Find function with path compression: 
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return
            # Set the smaller side to parent in dictionary order
            if root_x < root_y:
                parent[root_y] = root_x
            else:
                parent[root_x] = root_y
        
        for char1, char2 in zip(s1, s2):
            union(ord(char1) - ord('a'), ord(char2) - ord('a'))

        # Convert each character in baseStr to its smallest equivalent
        result = []
        for char in baseStr:
            smallest = chr(find(ord(char) - ord('a')) + ord('a')) #root + ord('a')
            result.append(smallest)

        return ''.join(result) 