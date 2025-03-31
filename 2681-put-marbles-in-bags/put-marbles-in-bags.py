class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # Put marbles in one bag so difference is 0
        if k == 1:
            return 0 
        
        # sum of adjacent marbles at each possible cut position
        diffs = [weights[i] + weights[i + 1] for i in range(len(weights) - 1)]
        diffs.sort()

        cuts_needed = k - 1 # The number of cuts needed is k-1

        # sum of the smallest k-1 values (Minimum partition cost)
        min_sum = sum(diffs[:cuts_needed])
        # sum of the largest k-1 values (Maximum partition cost)
        max_sum = sum(diffs[-cuts_needed:])

        return max_sum - min_sum