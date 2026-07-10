class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # 원래 인덱스를 기억하며 값 기준으로 정렬
        arr = sorted([(nums[i], i) for i in range(n)])
        
        # 원래 인덱스 -> 정렬된 배열의 인덱스로 매핑
        pos = [0] * n
        for idx, (val, original_idx) in enumerate(arr):
            pos[original_idx] = idx
            
        vals = [x[0] for x in arr]
        
        # DP 테이블 초기화 (최대 점프 횟수 log2(100000)는 대략 17이므로 18로 설정)
        LOG = 18
        left = [[0] * LOG for _ in range(n)]
        right = [[0] * LOG for _ in range(n)]
        
        # 1-Hop (2^0 = 1번 이동)으로 갈 수 있는 좌/우 끝 인덱스 계산
        for i in range(n):
            # vals 배열에서 vals[i] - maxDiff 보다 크거나 같은 첫 위치
            left[i][0] = bisect.bisect_left(vals, vals[i] - maxDiff)
            # vals 배열에서 vals[i] + maxDiff 보다 큰 첫 위치 - 1
            right[i][0] = bisect.bisect_right(vals, vals[i] + maxDiff) - 1
            
        # 2^k 번 이동했을 때의 좌/우 끝 점프 테이블 채우기
        for k in range(1, LOG):
            for i in range(n):
                L = left[i][k-1]
                R = right[i][k-1]
                # 정렬된 상태이므로, 가장 멀리 가는 것은 양 끝점에서 점프하는 것과 같음
                left[i][k] = left[L][k-1]
                right[i][k] = right[R][k-1]
                
        # 쿼리 처리
        answer = []
        for u, v in queries:
            if u == v:
                answer.append(0)
                continue
                
            start = pos[u]
            target = pos[v]
            
            # 아예 도달 불가능한 경우 (최대 점프인 2^(LOG-1)를 뛰어도 타겟이 구간 밖에 있음)
            if target < left[start][LOG-1] or target > right[start][LOG-1]:
                answer.append(-1)
                continue
                
            # 최소 이동 횟수 찾기 (Binary Lifting)
            curr_L = start
            curr_R = start
            jumps = 0
            
            # 큰 점프부터 시도하면서, 타겟에 '도달하지 못하는' 최대 점프들을 누적
            for k in range(LOG - 1, -1, -1):
                next_L = left[curr_L][k]
                next_R = right[curr_R][k]
                
                # 2^k 번 점프했는데도 타겟이 여전히 구간 밖이라면? -> 이 점프는 확정!
                if target < next_L or target > next_R:
                    curr_L = next_L
                    curr_R = next_R
                    jumps += (1 << k) # 2^k 회 누적
                    
            # 루프가 끝나면 타겟에 도달하기 딱 1보 직전의 상태가 되므로 +1을 해줌
            answer.append(jumps + 1)
            
        return answer