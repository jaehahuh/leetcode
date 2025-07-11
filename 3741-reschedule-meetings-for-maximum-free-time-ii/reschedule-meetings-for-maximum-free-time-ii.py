class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime) # number of meetings
        can_relocate_meeting = [False] * n

        max_gap_before_current_meeting = 0
        for i in range(n):
            current_meeting_duration = endTime[i] - startTime[i]
            if current_meeting_duration <= max_gap_before_current_meeting:
                can_relocate_meeting[i] = True
            gap_before_this_meeting = startTime[i] - (0 if i == 0 else endTime[i-1])
            max_gap_before_current_meeting = max(max_gap_before_current_meeting, gap_before_this_meeting)
        
        max_gap_after_current_meeting = 0
        for i in range(n - 1, -1, -1):
            current_meeting_duration = endTime[i] - startTime[i]
            if current_meeting_duration <= max_gap_after_current_meeting:
                can_relocate_meeting[i] = True
            gap_after_this_meeting = (eventTime if i == n - 1 else startTime[i+1]) - endTime[i]

            max_gap_after_current_meeting = max(max_gap_after_current_meeting, gap_after_this_meeting)

        max_overall_free_time = 0
        for i in range(n):
            interval_start_if_meeting_removed = 0 if i == 0 else endTime[i - 1]
            interval_end_if_meeting_removed = eventTime if i == n - 1 else startTime[i + 1]

            if can_relocate_meeting[i]:
                max_overall_free_time = max(max_overall_free_time, interval_end_if_meeting_removed - interval_start_if_meeting_removed)
            else:
                current_meeting_duration = endTime[i] - startTime[i]
                max_overall_free_time = max(max_overall_free_time, (interval_end_if_meeting_removed - interval_start_if_meeting_removed) - current_meeting_duration)
        
        return max_overall_free_time