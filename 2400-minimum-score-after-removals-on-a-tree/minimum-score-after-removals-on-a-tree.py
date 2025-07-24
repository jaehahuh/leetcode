class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        subtree_xor = [0] * n 
        tin = [0] * n         
        tout = [0] * n        
        
        timer = 0 

        def dfs(u: int, p: int) -> int:
            nonlocal timer
            
            tin[u] = timer
            timer += 1

            current_xor_sum = nums[u]
            
            for v in adj[u]:
                if v == p: 
                    continue
                current_xor_sum ^= dfs(v, u) 
            
            subtree_xor[u] = current_xor_sum
            tout[u] = timer
            timer += 1
            
            return current_xor_sum

        dfs(0, -1) 
        
        total_tree_xor_sum = subtree_xor[0]
        
        def is_ancestor(u: int, v: int) -> bool:
            return tin[u] <= tin[v] and tout[v] <= tout[u]

        min_score = float('inf') 
        
        num_edges = len(edges)

        for e1_idx in range(num_edges):
            for e2_idx in range(e1_idx + 1, num_edges):

                u1, v1 = edges[e1_idx]
                cut_node1 = v1 if is_ancestor(u1, v1) else u1

                u2, v2 = edges[e2_idx]
                cut_node2 = v2 if is_ancestor(u2, v2) else u2
                
                xor_s1 = subtree_xor[cut_node1]
                xor_s2 = subtree_xor[cut_node2]
                
                components_xor_values = []
                
                if is_ancestor(cut_node1, cut_node2):
                    components_xor_values.append(xor_s2)
                    components_xor_values.append(xor_s1 ^ xor_s2)
                    components_xor_values.append(total_tree_xor_sum ^ xor_s1)
                
                elif is_ancestor(cut_node2, cut_node1):
                    components_xor_values.append(xor_s1)
                    components_xor_values.append(xor_s2 ^ xor_s1)
                    components_xor_values.append(total_tree_xor_sum ^ xor_s2)
                
                else:
                    components_xor_values.append(xor_s1)
                    components_xor_values.append(xor_s2)
                    components_xor_values.append(total_tree_xor_sum ^ xor_s1 ^ xor_s2)
                
                current_score = max(components_xor_values) - min(components_xor_values)
                
                min_score = min(min_score, current_score)
                
        return min_score