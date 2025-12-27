class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        empty_rooms = [i for i in range(n)]
        heapq.heapify(empty_rooms)

        occupied_rooms = []
        count = [0] * n
        for start, end in meetings:
            while occupied_rooms and occupied_rooms[0][0] <= start:
                end_time, room_id = heapq.heappop(occupied_rooms)
                heapq.heappush(empty_rooms, room_id)

            if empty_rooms:
                room_id = heapq.heappop(empty_rooms)
                heapq.heappush(occupied_rooms, (end, room_id))
            else:
                earliest_end_time, room_id = heapq.heappop(occupied_rooms)
                new_end = earliest_end_time + (end - start)
                heapq.heappush(occupied_rooms, (new_end, room_id))
            
            count[room_id] += 1
            
        max_meetings = -1
        result = -1
        for i in range(n):
            if count[i] > max_meetings:
                max_meetings = count[i]
                result = i

        return result