class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        sorted_intervals = sorted(
            (l, r, w, idx) for idx, (l, r, w) in enumerate(intervals)
        )

        starts = [interval[0] for interval in sorted_intervals]

        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            l, r, weight, orig_idx = sorted_intervals[i]
            
            # 현재 구간 선택 시, 경계가 겹치지 않는 다음 구간 위치 찾기 (start >= r + 1)
            next_idx = bisect_left(starts, r + 1)
            
            for k in range(1, 5):
                # 선택지 1: 현재 구간을 건너뛰는 경우 (Skip)
                skip_weight, skip_indices = dp[i + 1][k]
                
                # 선택지 2: 현재 구간을 선택하는 경우 (Pick)
                next_weight, next_indices = dp[next_idx][k - 1]
                pick_weight = weight + next_weight
                pick_indices = sorted([orig_idx] + next_indices)
                
                # 두 선택지 중 최적의 값 선택
                if pick_weight > skip_weight:
                    dp[i][k] = (pick_weight, pick_indices)
                elif skip_weight > pick_weight:
                    dp[i][k] = (skip_weight, skip_indices)
                else:
                    # 가중치가 같으면 사전순으로 더 작은 인덱스 조합 선택
                    dp[i][k] = (pick_weight, min(pick_indices, skip_indices))
        
        # 첫 번째 구간부터 탐색하며 최대 4개 선택한 결과 반환
        return dp[0][4][1]