class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        max_heap = [] 
        min_heap = [] 
    
        sum_lower = 0
        sum_upper = 0
        delayed = defaultdict(int) # lazy deletion을 위한 백로그

        def prune(heap):
            while heap:
                val = -heap[0] if heap is max_heap else heap[0]
                if delayed[val] > 0:
                    delayed[val] -= 1
                    heapq.heappop(heap)
                else:
                    break
                
        cost = [0] * (n - x + 1)
        
        # 초반 윈도우 빌드 및 슬라이딩 진행
        lower_size = 0
        upper_size = 0
        
        for i in range(n):
            val = nums[i]
            
            # 요소 삽입
            if not max_heap or val <= -max_heap[0]:
                heapq.heappush(max_heap, -val)
                sum_lower += val
                lower_size += 1
            else:
                heapq.heappush(min_heap, val)
                sum_upper += val
                upper_size += 1
                
            # 범위 이탈 요소 제거 (i >= x)
            if i >= x:
                out_val = nums[i - x]
                delayed[out_val] += 1
                if out_val <= -max_heap[0]:
                    sum_lower -= out_val
                    lower_size -= 1
                    if out_val == -max_heap[0]:
                        prune(max_heap)
                else:
                    sum_upper -= out_val
                    upper_size -= 1
                    if out_val == min_heap[0]:
                        prune(min_heap)
                        
            # 힙 균형 조절
            while lower_size < upper_size:
                prune(min_heap)
                moved = heapq.heappop(min_heap)
                sum_upper -= moved
                upper_size -= 1
                heapq.heappush(max_heap, -moved)
                sum_lower += moved
                lower_size += 1
                
            while lower_size > upper_size + 1:
                prune(max_heap)
                moved = -heapq.heappop(max_heap)
                sum_lower -= moved
                lower_size -= 1
                heapq.heappush(min_heap, moved)
                sum_upper += moved
                upper_size += 1
                
            prune(max_heap)
            prune(min_heap)
            
            # 윈도우 완성 시 연산 비용 기록
            if i >= x - 1:
                median = -max_heap[0]
                current_cost = (median * lower_size - sum_lower) + (sum_upper - median * upper_size)
                cost[i - x + 1] = current_cost

        # DP: k개의 비중복 길이 x 구간 선택
        # dp[j] = j개의 구간을 선택했을 때의 최소 비용
        dp = [float('inf')] * (k + 1)
        dp[0] = 0
        
        # 1D DP 갱신 (전방 방향 또는 역방향 갱신)
        # dp_table[i][j] = min(dp_table[i+1][j], cost[i] + dp_table[i+x][j-1])
        dp_matrix = [[float('inf')] * (k + 1) for _ in range(n + 2)]
        for i in range(n + 1):
            dp_matrix[i][0] = 0
            
        for i in range(n - x, -1, -1):
            for j in range(1, k + 1):
                dp_matrix[i][j] = dp_matrix[i + 1][j]
                if i + x <= n:
                    dp_matrix[i][j] = min(dp_matrix[i][j], cost[i] + dp_matrix[i + x][j - 1])
                    
        return dp_matrix[0][k]