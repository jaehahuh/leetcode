class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda item: item[1])
        indexed_queries = sorted(enumerate(queries), key=lambda item: item[1])
        
        res = [0] * len(queries)
        
        left = 0
        right = 0
        num_logs = len(logs)
        server_counts = {}
        active_servers = 0
        
        for original_idx, q in indexed_queries:
            window_start = q - x
            window_end = q
            
            while right < num_logs and logs[right][1] <= window_end:
                s_id = logs[right][0]
                if server_counts.get(s_id, 0) == 0:
                    active_servers += 1
                server_counts[s_id] = server_counts.get(s_id, 0) + 1
                right += 1

            while left < num_logs and logs[left][1] < window_start:
                s_id = logs[left][0]
                server_counts[s_id] -= 1
                if server_counts[s_id] == 0:
                    active_servers -= 1
                left += 1

            res[original_idx] = n - active_servers
            
        return res