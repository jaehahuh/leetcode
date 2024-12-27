class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        result = 0
        current_max = values[0] - 1 # initialize with the first value - position
        for i in range(1, len(values)):
            result = max(result, current_max + values[i]) # update the maximum score with the current pair
            current_max = max(current_max-1, values[i]-1)  # update current_max considering the distance
        return result