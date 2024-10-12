class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        for start, end in intervals:
            events.append((start, 1))  #startpoint
            events.append((end+1, -1))  #end points 

        events.sort() #sort by time

        max_groups = 0
        cur_groups = 0

        for i, event in events:
            cur_groups += event
            max_groups = max(max_groups, cur_groups)
        
        return(max_groups)