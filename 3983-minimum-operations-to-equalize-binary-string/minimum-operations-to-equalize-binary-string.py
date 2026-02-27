class Solution:
    def minOperations(self, s: str, k: int) -> int:
        length = len(s)
        parity_sets = [SortedSet() for _ in range(2)]  # 짝수, 홀수 상태 집합 생성
        for zeros_count in range(length + 1):
            parity_sets[zeros_count % 2].add(zeros_count)  # 0의 개수에 따라 해당 parity 집합에 추가
        
        current_zeros = s.count('0') 
        parity_sets[current_zeros % 2].remove(current_zeros)
        
        queue = deque([current_zeros])  # BFS 큐 초기화
        operations = 0  
        
        while queue:
            for _ in range(len(queue)):
                zeros_in_state = queue.popleft()  # 현재 0 개수 상태
                
                if zeros_in_state == 0:
                    return operations  
                
                # 다음 상태 가능한 0 개수 범위 계산
                left_bound = zeros_in_state + k - 2 * min(zeros_in_state, k)
                right_bound = zeros_in_state + k - 2 * max(k - length + zeros_in_state, 0)
                target_parity = left_bound % 2  # 다음 상태 parity
                
                states_set = parity_sets[target_parity]  # parity에 맞는 상태 집합 선택
                
                # 범위 내 가능한 다음 상태들 이분 탐색 시작 위치
                start_index = states_set.bisect_left(left_bound)
                
                # 범위 내 모든 상태에 대해 방문 처리 및 큐 추가
                while start_index < len(states_set) and states_set[start_index] <= right_bound:
                    next_state = states_set[start_index]
                    queue.append(next_state)
                    states_set.remove(next_state) 
            
            operations += 1  
        
        return -1  