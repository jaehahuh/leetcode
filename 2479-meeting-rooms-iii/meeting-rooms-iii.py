class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        available_rooms = [i for i in range(n)]
        heapq.heapify(available_rooms)

        occupied_rooms = []
        meeting_counts = [0] * n

        for start, end in meetings:
            while occupied_rooms and occupied_rooms[0][0] <= start:
                _end_time, room_id = heapq.heappop(occupied_rooms)
                heapq.heappush(available_rooms, room_id)

            if available_rooms:
                room_id = heapq.heappop(available_rooms)
                heapq.heappush(occupied_rooms, (end, room_id))
            else:
                earliest_end_time, room_id = heapq.heappop(occupied_rooms)
                new_end = earliest_end_time + (end - start)
                heapq.heappush(occupied_rooms, (new_end, room_id))

            meeting_counts[room_id] += 1

        max_meetings = -1
        result_room = -1
        for i in range(n):
            if meeting_counts[i] > max_meetings:
                max_meetings = meeting_counts[i]
                result_room = i

        return result_room