class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        attended_count = 0
        min_heap = [] # 현재 참석 가능한 이벤트들의 종료일을 저장하는 최소 힙
        i = 0
        max_day = max(event[1] for event in events) #최대 종료일
        for day in range(1, max_day + 1):
            while i < len(events) and events[i][0] == day:
                heapq.heappush(min_heap, events[i][1]) # 힙에는 이벤트의 종료일을 저장
                i += 1
            
            # min_heap에서 현재 날짜보다 종료일이 빠른 이벤트를 제거
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
            
            # min_heap에 아직 참석 가능한 이벤트가 있다면, 그 중 종료일이 가장 빠른 이벤트를 선택 후 참석
            if min_heap:
                heapq.heappop(min_heap)
                attended_count += 1
            
        return attended_count