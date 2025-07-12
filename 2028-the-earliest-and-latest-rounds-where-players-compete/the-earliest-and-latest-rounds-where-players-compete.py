class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        # Ensure firstPlayer is always smaller than secondPlayer for consistent processing
        firstPlayer, secondPlayer = min(firstPlayer, secondPlayer), max(firstPlayer, secondPlayer)
        memo = {}
        def dfs(players):
            if players in memo:
                return memo[players]

            num_current_players = len(players)
            # Check if firstPlayer and secondPlayer are still in the current round
            try:
                fp_idx = players.index(firstPlayer)
                sp_idx = players.index(secondPlayer)
            except ValueError:
                # If either player is eliminated, they cannot meet. Return infinity.
                return (float('inf'), float('-inf'))

            # Check if the two players meet in the current round
            if fp_idx + sp_idx == num_current_players - 1:
                memo[players] = (1, 1)
                return (1, 1)

            # If they don't meet in this round, simulate all possible outcomes for the next round
            min_next_round_cost = float('inf')
            max_next_round_cost = -float('inf')

            def generate_next_round_states(l_idx, r_idx, current_winners_list):
                nonlocal min_next_round_cost, max_next_round_cost

                if l_idx >= r_idx:
                    # If odd number of players, the middle one advances automatically
                    if l_idx == r_idx: 
                        current_winners_list.append(players[l_idx])

                    # Sort and convert to tuple for memoization key
                    next_players_tuple = tuple(sorted(current_winners_list))

                    # Recursively call dfs for the next round
                    res_min, res_max = dfs(next_players_tuple)
                    
                    # Update min/max rounds by adding 1 (for the current round)
                    min_next_round_cost = min(min_next_round_cost, 1 + res_min)
                    max_next_round_cost = max(max_next_round_cost, 1 + res_max)

                    # Backtrack: remove the middle player if added
                    if l_idx == r_idx:
                        current_winners_list.pop()
                    return

                p1, p2 = players[l_idx], players[r_idx]

                if p1 == firstPlayer or p1 == secondPlayer:
                    # Only consider p1 winning to ensure target players survive
                    generate_next_round_states(l_idx + 1, r_idx - 1, current_winners_list + [p1])
                elif p2 == firstPlayer or p2 == secondPlayer:
                    # Only consider p2 winning to ensure target players survive
                    generate_next_round_states(l_idx + 1, r_idx - 1, current_winners_list + [p2])
                else:
                    # Explore both possibilities: p1 wins or p2 wins
                    generate_next_round_states(l_idx + 1, r_idx - 1, current_winners_list + [p1])
                    generate_next_round_states(l_idx + 1, r_idx - 1, current_winners_list + [p2])

            # Start backtracking from the outermost pair
            generate_next_round_states(0, num_current_players - 1, [])
            
            memo[players] = (min_next_round_cost, max_next_round_cost)
            return (min_next_round_cost, max_next_round_cost)

        return list(dfs(tuple(range(1, n + 1))))