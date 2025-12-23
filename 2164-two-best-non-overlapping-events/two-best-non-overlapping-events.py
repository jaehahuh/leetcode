class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort(key=lambda x: x[0]) # Sorted by startTime
        
        max_val_from_i = [0] * (n+1)
        for i in range(n - 1, -1, -1):
            max_val_from_i[i] = max(events[i][2], max_val_from_i[i+1])
        
        event_starts = [event[0] for event in events]
        
        max_total = 0
        for i in range(n):
            curr_val = events[i][2]
            curr_end = events[i][1]

            max_total = max(max_total, curr_val)
            next_event_starts = curr_end + 1
            next_i = bisect.bisect_left(event_starts, next_event_starts)

            if next_i < n:
                max_val_next_events = max_val_from_i[next_i]
                max_total = max(max_total, curr_val + max_val_next_events)
            
        return max_total