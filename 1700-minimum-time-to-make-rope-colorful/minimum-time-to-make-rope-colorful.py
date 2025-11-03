class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        min_time = 0

        current_group_max_time = neededTime[0]
        current_group_total_time = neededTime[0]

        for i in range(1, len(colors)):
            if colors[i-1] == colors[i]:
                current_group_max_time = max(current_group_max_time, neededTime[i])
                current_group_total_time += neededTime[i]
            else:
                min_time += (current_group_total_time - current_group_max_time)

                #start new current group
                current_group_max_time = neededTime[i]
                current_group_total_time = neededTime[i]
        
        min_time += (current_group_total_time - current_group_max_time)
        return min_time