class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        # dp_score: 도달할 수 없는 곳은 -1로 초기화
        dp_score = [[-1] * n for _ in range(n)]
        # dp_count: 경로의 수 초기화
        dp_count = [[0] * n for _ in range(n)]

        dp_score[n-1][n-1] = 0
        dp_count[n-1][n-1] = 1

        # 우측 하단에서 좌측 상단으로 역순 탐색
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                # 시작점이거나 장애물이면 스킵
                if (r == n - 1 and c == n - 1) or board[r][c] == 'X':
                    continue
                
                # 이전 이동 경로 후보 (아래, 오른쪽, 우측 하단 대각선)
                max_prev_score = -1
                if r + 1 < n and dp_score[r+1][c] != -1:
                    max_prev_score = max(max_prev_score, dp_score[r+1][c])
                if c + 1 < n and dp_score[r][c+1] != -1:
                    max_prev_score = max(max_prev_score, dp_score[r][c+1])
                if r + 1 < n and c + 1 < n and dp_score[r+1][c+1] != -1:
                    max_prev_score = max(max_prev_score, dp_score[r+1][c+1])
                
                # 도달 가능한 이전 경로가 없는 경우 (고립된 경우)
                if max_prev_score == -1:
                    continue
                
                # 1. 최대 점수 계산 ('E'는 0점으로 처리)
                current_val = 0 if board[r][c] == 'E' else int(board[r][c])
                dp_score[r][c] = max_prev_score + current_val
                
                # 2. 경로의 수 합산 (최대 점수를 만들어낸 이전 경로들만 더함)
                paths = 0
                if r + 1 < n and dp_score[r+1][c] == max_prev_score:
                    paths = (paths + dp_count[r+1][c]) % MOD
                if c + 1 < n and dp_score[r][c+1] == max_prev_score:
                    paths = (paths + dp_count[r][c+1]) % MOD
                if r + 1 < n and c + 1 < n and dp_score[r+1][c+1] == max_prev_score:
                    paths = (paths + dp_count[r+1][c+1]) % MOD
                    
                dp_count[r][c] = paths
                
        # 최종 도착점에 도달하지 못한 경우(dp_score가 -1) 예외 처리
        max_score = max(0, dp_score[0][0])
        return [max_score, dp_count[0][0]]