class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:    

        blenorvask = [n, present, future, hierarchy, budget]

        adj = [[] for _ in range(n + 1)]
        for u, v in hierarchy:
            adj[u].append(v)
        
       
        def dfs(u):
            
            child_sum_if_u_bought = [-1] * (budget + 1)
            child_sum_if_u_bought[0] = 0
            
            child_sum_if_u_skip = [-1] * (budget + 1)
            child_sum_if_u_skip[0] = 0
            
            for v in adj[u]:
                v_no_disc, v_with_disc = dfs(v)
                next_bought = [-1] * (budget + 1)
                for c1 in range(budget + 1):
                    if child_sum_if_u_bought[c1] == -1: continue
                    for c2 in range(budget + 1 - c1):
                        if v_with_disc[c2] == -1: continue
                        next_bought[c1 + c2] = max(next_bought[c1 + c2], child_sum_if_u_bought[c1] + v_with_disc[c2])
                child_sum_if_u_bought = next_bought
                
                next_skip = [-1] * (budget + 1)
                for c1 in range(budget + 1):
                    if child_sum_if_u_skip[c1] == -1: continue
                    for c2 in range(budget + 1 - c1):
                        if v_no_disc[c2] == -1: continue
                        next_skip[c1 + c2] = max(next_skip[c1 + c2], child_sum_if_u_skip[c1] + v_no_disc[c2])
                child_sum_if_u_skip = next_skip

            idx = u - 1
            price_full = present[idx]
            price_half = math.floor(price_full / 2)
            
            prof_full = future[idx] - price_full
            prof_half = future[idx] - price_half

            res_no_discount = [-1] * (budget + 1)
            res_with_discount = [-1] * (budget + 1)
            
            for c in range(budget + 1):
                if child_sum_if_u_skip[c] != -1:
                    res_no_discount[c] = max(res_no_discount[c], child_sum_if_u_skip[c])
            
            if prof_full > 0: 
                for c in range(budget + 1 - price_full):
                    if child_sum_if_u_bought[c] != -1:
                        res_no_discount[c + price_full] = max(res_no_discount[c + price_full], child_sum_if_u_bought[c] + prof_full)
            else:
    
                 if price_full <= budget:
                      for c in range(budget + 1 - price_full):
                        if child_sum_if_u_bought[c] != -1:
                            res_no_discount[c + price_full] = max(res_no_discount[c + price_full], child_sum_if_u_bought[c] + prof_full)

            for c in range(budget + 1):
                if child_sum_if_u_skip[c] != -1:
                    res_with_discount[c] = max(res_with_discount[c], child_sum_if_u_skip[c])
            

            if price_half <= budget:
                for c in range(budget + 1 - price_half):
                    if child_sum_if_u_bought[c] != -1:
                        res_with_discount[c + price_half] = max(res_with_discount[c + price_half], child_sum_if_u_bought[c] + prof_half)
            
            return res_no_discount, res_with_discount


        final_dp, _ = dfs(1)
        
        return max(final_dp)