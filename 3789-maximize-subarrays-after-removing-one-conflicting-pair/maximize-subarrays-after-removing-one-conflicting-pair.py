class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        INF = float('inf') 
        min_b_for_a, second_min_b_for_a = self.preprocess_pairs(n, conflictingPairs, INF)
        total_valid_no_removal, gains_by_a = self.sweep_from_right(
            n, min_b_for_a, second_min_b_for_a, INF
        )
        return total_valid_no_removal + max(gains_by_a)

    def preprocess_pairs(self, n, pairs, inf_val):

        min_b_for_a = [inf_val] * (n + 1)
        second_min_b_for_a = [inf_val] * (n + 1)

        for p1, p2 in pairs: 
            start_idx = min(p1, p2) 
            end_idx = max(p1, p2)   

            if min_b_for_a[start_idx] > end_idx:
                second_min_b_for_a[start_idx] = min_b_for_a[start_idx]
                min_b_for_a[start_idx] = end_idx
            elif second_min_b_for_a[start_idx] > end_idx:
                second_min_b_for_a[start_idx] = end_idx
        
        return min_b_for_a, second_min_b_for_a

    def sweep_from_right(self, n, min_b_for_a, second_min_b_for_a,inf_val) :

        total_valid_no_removal = 0
        curr_restrict_a = n 

        next_restrict_b_global = inf_val
        gains_by_a = [0] * (n + 1)

        for i in range(n, 0, -1):
            if min_b_for_a[curr_restrict_a] > min_b_for_a[i]:
                next_restrict_b_global = min(next_restrict_b_global, min_b_for_a[curr_restrict_a])
                curr_restrict_a = i 
            else:
                next_restrict_b_global = min(next_restrict_b_global, min_b_for_a[i])

            valid_end = min(min_b_for_a[curr_restrict_a], n + 1)
            total_valid_no_removal += (valid_end - i)

            original_valid_end = valid_end
            
            new_valid_end = min(
                min(next_restrict_b_global, second_min_b_for_a[curr_restrict_a]), n + 1
            )
            
            gains_by_a[curr_restrict_a] += (new_valid_end - original_valid_end)

        return total_valid_no_removal, gains_by_a