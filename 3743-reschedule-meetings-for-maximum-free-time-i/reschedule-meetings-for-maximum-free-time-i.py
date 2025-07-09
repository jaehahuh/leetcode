class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)

        if n == 0:
            return eventTime

        gaps = []
        gaps.append(startTime[0])
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i-1])
        gaps.append(eventTime - endTime[n-1])

        if len(gaps) <= k + 1:
            return sum(gaps)

        window_sum = sum(gaps[i] for i in range(k + 1))
        max_free_time = window_sum

        for i in range(k + 1, len(gaps)):
            window_sum += gaps[i] - gaps[i - (k + 1)]
            max_free_time = max(max_free_time, window_sum)

        return max_free_time