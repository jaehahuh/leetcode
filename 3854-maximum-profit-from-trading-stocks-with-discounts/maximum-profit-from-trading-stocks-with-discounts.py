class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:    
        adj = [[] for _ in range(n + 1)]
        for u, v in hierarchy:
            adj[u].append(v)
        
        memo = {}
       
        def dfs(u):
            if u in memo:
                return memo[u]
            
            child_sum_if_u_bought = [-float('inf')] * (budget + 1)
            child_sum_if_u_bought[0] = 0
            
            child_sum_if_u_skip = [-float('inf')] * (budget + 1)
            child_sum_if_u_skip[0] = 0
            
            for v in adj[u]:
                v_no_disc_res, v_with_disc_res = dfs(v)

                next_bought = [-float('inf')] * (budget + 1)
                for c1 in range(budget + 1):
                    if child_sum_if_u_bought[c1] == -float('inf'): continue
                    for c2 in range(budget + 1 - c1):
                        if v_with_disc_res[c2] == -float('inf'): continue
                        next_bought[c1 + c2] = max(next_bought[c1 + c2], child_sum_if_u_bought[c1] + v_with_disc_res[c2])
                child_sum_if_u_bought = next_bought
                
                next_skip = [-float('inf')] * (budget + 1)
                for c1 in range(budget + 1):
                    if child_sum_if_u_skip[c1] == -float('inf'): continue
                    for c2 in range(budget + 1 - c1):
                        if v_no_disc_res[c2] == -float('inf'): continue
                        next_skip[c1 + c2] = max(next_skip[c1 + c2], child_sum_if_u_skip[c1] + v_no_disc_res[c2])
                child_sum_if_u_skip = next_skip

            idx = u - 1
            price_full = present[idx]
            profit_full = future[idx] - price_full
            
            price_half = math.floor(present[idx] / 2)
            profit_half = future[idx] - price_half

            res_no_discount = [-float('inf')] * (budget + 1)
            res_with_discount = [-float('inf')] * (budget + 1)
            
            for c in range(budget + 1):
                if child_sum_if_u_skip[c] != -float('inf'):
                    res_no_discount[c] = max(res_no_discount[c], child_sum_if_u_skip[c])
            
            if price_full <= budget:
                for c_child_sum in range(budget + 1 - price_full):
                    if child_sum_if_u_bought[c_child_sum] != -float('inf'):
                        res_no_discount[c_child_sum + price_full] = max(
                            res_no_discount[c_child_sum + price_full],
                            child_sum_if_u_bought[c_child_sum] + profit_full
                        )

            for c in range(budget + 1):
                if child_sum_if_u_skip[c] != -float('inf'):
                    res_with_discount[c] = max(res_with_discount[c], child_sum_if_u_skip[c])
            
            if price_half <= budget:
                for c_child_sum in range(budget + 1 - price_half):
                    if child_sum_if_u_bought[c_child_sum] != -float('inf'):
                        res_with_discount[c_child_sum + price_half] = max(
                            res_with_discount[c_child_sum + price_half],
                            child_sum_if_u_bought[c_child_sum] + profit_half
                        )
            
            memo[u] = (res_no_discount, res_with_discount)
            return res_no_discount, res_with_discount

        final_dp_for_ceo, _ = dfs(1)
        
        max_total_profit = 0
        for profit_val in final_dp_for_ceo:
            max_total_profit = max(max_total_profit, profit_val)
            
        return max_total_profit