class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        len_s = len(servers)
        len_t = len(tasks)
        free_servers = [(servers[i], i) for i in range(len_s)]
        heapq.heapify(free_servers)

        busy_servers = []
        curr_time = 0
        result = [0] * len_t

        for i in range(len_t):
            # 현재 시간이 작업 i의 도착 시간보다 빠를 수 있으므로 max(current_time, i)로 설정
            curr_time = max(curr_time, i)

            # 만약 사용 가능한 서버가 없다면, 가장 빨리 끝나는 서버의 시간으로 점프
            if not free_servers and busy_servers[0][0] > curr_time:
                curr_time = busy_servers[0][0]
            
            # 현재 시간 기준으로 일이 끝난 서버들을 free_servers로 이동
            while busy_servers and busy_servers[0][0] <= curr_time:
                _, w, idx = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (w, idx))
            
            # 가장 우선순위가 높은 서버 할당
            weight, index = heapq.heappop(free_servers)
            result[i] = index

            # 작업이 끝나는 시간을 계산하여 busy_servers에 추가
            duration = tasks[i]
            heapq.heappush(busy_servers, (curr_time + duration, weight, index))
        
        return result