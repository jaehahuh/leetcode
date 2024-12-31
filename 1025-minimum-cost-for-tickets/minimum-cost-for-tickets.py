class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Convert the list of travel days into a set for faster lookups
        days_set = set(days)
        # Create a DP array to store the minimum cost up to each day
        dp = [0] * (days[-1] + 1)

        for day in range(1, days[-1] + 1):
            if day not in days_set:
                # If this day is not a travel day, cost remains the same as the previous day
                dp[day] = dp[day - 1]
            else:
                # If this day is a travel day, calculate the minimum cost among the three ticket options
                dp[day] = min( dp[max(0, day - 1)] + costs[0], dp[max(0, day - 7)] + costs[1],  
                dp[max(0, day - 30)] + costs[2])
    
        return dp[days[-1]]