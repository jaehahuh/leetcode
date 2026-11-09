class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        busy_servers = []
        available_servers = list(range(k))
        request_count = [0] * k

        for i, (arr_time, l_time) in enumerate(zip(arrival, load)):
            while busy_servers and busy_servers[0][0] <= arr_time:
                _, server_id = heapq.heappop(busy_servers)
                
                idx = bisect_left(available_servers, server_id)
                if idx == len(available_servers) or available_servers[idx] != server_id:
                    insort(available_servers, server_id, lo=idx)

            if not available_servers:
                continue
            
            pref = i % k
            idx = bisect_left(available_servers, pref)
            
            if idx == len(available_servers):
                idx = 0
            
            target_server = available_servers.pop(idx)
            
            request_count[target_server] += 1
            
            heapq.heappush(busy_servers, (arr_time + l_time, target_server))
            
        max_requests = max(request_count)

        return [i for i, count in enumerate(request_count) if count == max_requests]