class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        start_days = [event[0] for event in events]
        n = len(events)
        memo = {}

        def dp(idx, remaining):
            if idx == n or remaining == 0:
                return 0

            if (idx, remaining) in memo:
                return memo[(idx, remaining)]
            
            skip_current_event_value = dp(idx + 1, remaining)
            current_event_value = events[idx][2]
            current_event_end_day = events[idx][1]

            next_event_idx = bisect_right(start_days, current_event_end_day)

            attend_current_event_value = current_event_value + dp(next_event_idx, remaining - 1)
            result = max(skip_current_event_value, attend_current_event_value)
            memo[(idx, remaining)] = result
            return result

        return dp(0, k)