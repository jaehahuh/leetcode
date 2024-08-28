class MyCalendarThree:

    def __init__(self):
        #it store changes in event count at specific times
        self.timeline = collections.defaultdict(int)

    def book(self, startTime: int, endTime: int) -> int:
        # increment count at startTime, decrement count at endTime
        self.timeline[startTime] += 1
        self.timeline[endTime] -= 1

        #Sweep line algorithm to find the maximum overlap
        ongoing = 0
        max_k = 0

        for t in sorted(self.timeline):
            ongoing += self.timeline[t]
            max_k = max(max_k, ongoing)
        
        return max_k