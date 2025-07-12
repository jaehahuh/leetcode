class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        firstPlayer, secondPlayer = min(firstPlayer, secondPlayer), max(firstPlayer, secondPlayer)
        memo = {}
        def dfs(players):
            if players in memo:
                return memo[players]

            num_current_players = len(players)

            try:
                fp_idx = players.index(firstPlayer)
                sp_idx = players.index(secondPlayer)
            except ValueError:
                return (float('inf'), float('-inf'))

            if fp_idx + sp_idx == num_current_players - 1:
                memo[players] = (1, 1)
                return (1, 1)

            min_next_round_cost = float('inf')
            max_next_round_cost = -float('inf')

            def generate_next_round_states(l_idx, r_idx, current_winners_list):
                nonlocal min_next_round_cost, max_next_round_cost

                if l_idx >= r_idx:
                    if l_idx == r_idx: 
                        current_winners_list.append(players[l_idx])

                    next_players_tuple = tuple(sorted(current_winners_list))
                    
                    res_min, res_max = dfs(next_players_tuple)
                
                    min_next_round_cost = min(min_next_round_cost, 1 + res_min)
                    max_next_round_cost = max(max_next_round_cost, 1 + res_max)

                    if l_idx == r_idx:
                        current_winners_list.pop()
                    return

                p1, p2 = players[l_idx], players[r_idx]

                if p1 == firstPlayer or p1 == secondPlayer:
                    generate_next_round_states(l_idx + 1, r_idx - 1, current_winners_list + [p1])
                elif p2 == firstPlayer or p2 == secondPlayer:
                    generate_next_round_states(l_idx + 1, r_idx - 1, current_winners_list + [p2])
                else:
                    generate_next_round_states(l_idx + 1, r_idx - 1, current_winners_list + [p1])
                    generate_next_round_states(l_idx + 1, r_idx - 1, current_winners_list + [p2])

            generate_next_round_states(0, num_current_players - 1, [])
            
            memo[players] = (min_next_round_cost, max_next_round_cost)
            return (min_next_round_cost, max_next_round_cost)

        return list(dfs(tuple(range(1, n + 1))))