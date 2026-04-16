from bisect import bisect_left

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        pos_map = defaultdict(list)
        for i, val in enumerate(nums):
            pos_map[val].append(i)
        
        results = []
        for q_idx in queries:
            target_val = nums[q_idx]
            indices = pos_map[target_val]
            
            # 해당 숫자가 하나뿐이면 -1
            if len(indices) <= 1:
                results.append(-1)
                continue
            
            # 이진 탐색으로 현재 인덱스의 위치 찾기
            idx_in_list = bisect_left(indices, q_idx)
            
            min_dist = float('inf')
            
            # 인접한 인덱스들 확인
            # 왼쪽(이전) 인덱스와의 거리
            prev_idx = indices[(idx_in_list - 1) % len(indices)]
            dist_prev = abs(q_idx - prev_idx)
            min_dist = min(min_dist, dist_prev, n - dist_prev)
            
            # 오른쪽(다음) 인덱스와의 거리
            next_idx = indices[(idx_in_list + 1) % len(indices)]
            dist_next = abs(q_idx - next_idx)
            min_dist = min(min_dist, dist_next, n - dist_next)
            
            results.append(min_dist)
            
        return results