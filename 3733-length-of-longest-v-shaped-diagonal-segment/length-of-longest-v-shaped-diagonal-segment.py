class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        # 방향: 0:↘(DR), 1:↙(DL), 2:↖(UL), 3:↗(UR)
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        cw = [1, 2, 3, 0]  # 시계방향 회전 매핑

        def next_sym(x: int) -> int:
            # 1->2, 2->0, 0->2
            if x == 2:
                return 0
            else:
                return 2

        def last_sym_from_len(L: int) -> int:
            if L == 1:
                return 1
            if L % 2 == 0:
                return 2
            else:
                return 0

        # 1) B1[d][i][j]: 방향 d로 진행하며 (i,j)에서 끝나는
        #    "1로 시작하는" 최장 길이
        B1 = [[[0]*m for _ in range(n)] for _ in range(4)]

        # 각 방향마다, 그 방향으로 나아가는 '라인'을 따라 스캔
        def compute_B1_for_direction(didx: int):
            dx, dy = dirs[didx]

            # 대각선 라인의 시작점들을 열거
            starts = []

            # 경계에서 시작하는 라인들: 위쪽 행과 좌/우쪽 열에서 시작
            # 방향으로 전진했을 때 격자 내를 훑도록 시작점 구성
            if dx == 1 and dy == 1:         # ↘: top row and left col
                for j in range(m):
                    starts.append((0, j))
                for i in range(1, n):
                    starts.append((i, 0))
            elif dx == 1 and dy == -1:      # ↙: top row and right col
                for j in range(m):
                    starts.append((0, j))
                for i in range(1, n):
                    starts.append((i, m-1))
            elif dx == -1 and dy == -1:     # ↖: bottom row and right col
                for j in range(m):
                    starts.append((n-1, j))
                for i in range(n-2, -1, -1):
                    starts.append((i, m-1))
            else:                            # ↗: bottom row and left col
                for j in range(m):
                    starts.append((n-1, j))
                for i in range(n-2, -1, -1):
                    starts.append((i, 0))

            for si, sj in starts:
                i, j = si, sj
                prev_len = 0  # 직전 칸에서 끝나는 1-start 패턴 길이
                while 0 <= i < n and 0 <= j < m:
                    val = grid[i][j]
                    new_len = 0
                    # 이어서 기대되는 값 계산
                    if prev_len > 0:
                        if prev_len == 1:
                            expect = 2
                        elif prev_len % 2 == 0:  # 짝수(>=2): last=2 → next=0
                            expect = 0
                        else:                    # 홀수(>=3): last=0 → next=2
                            expect = 2
                        if val == expect:
                            new_len = prev_len + 1

                    # 새로 시작(값이 1이면)
                    if val == 1:
                        new_len = max(new_len, 1)

                    # 둘 다 아니면 0
                    prev_len = new_len
                    B1[didx][i][j] = prev_len

                    i += dx
                    j += dy

        for d in range(4):
            compute_B1_for_direction(d)

        # 2) F[d][s][i][j]: 방향 d로 진행하며 (i,j)에서 시작,
        #    현재 칸 기대값이 s일 때 이어갈 수 있는 최장 길이
        # s ∈ {0,1,2}
        F = [[[[0]*m for _ in range(n)] for _ in range(3)] for _ in range(4)]

        def compute_F_for_direction(didx: int):
            dx, dy = dirs[didx]

            # next가 (i+dx, j+dy)이므로, 그 반대 순서로 스캔
            # ↘(1,1): i desc, j desc
            # ↙(1,-1): i desc, j asc
            # ↖(-1,-1): i asc, j asc
            # ↗(-1,1): i asc, j desc
            if dx == 1 and dy == 1:
                irange = range(n-1, -1, -1)
                jrange = range(m-1, -1, -1)
            elif dx == 1 and dy == -1:
                irange = range(n-1, -1, -1)
                jrange = range(0, m, 1)
            elif dx == -1 and dy == -1:
                irange = range(0, n, 1)
                jrange = range(0, m, 1)
            else:  # dx==-1, dy==1
                irange = range(0, n, 1)
                jrange = range(m-1, -1, -1)

            for i in irange:
                for j in jrange:
                    ni, nj = i + dx, j + dy
                    for s in (0, 1, 2):
                        if grid[i][j] != s:
                            F[didx][s][i][j] = 0
                        else:
                            add = 1
                            # 다음 칸에서 기대값 갱신
                            ns = next_sym(s)
                            if 0 <= ni < n and 0 <= nj < m:
                                add += F[didx][ns][ni][nj]
                            F[didx][s][i][j] = add

        for d in range(4):
            compute_F_for_direction(d)

        # 3) 정답 계산
        ans = 0
        # (a) 회전 없이
        for d in range(4):
            for i in range(n):
                for j in range(m):
                    if B1[d][i][j] > ans:
                        ans = B1[d][i][j]

        # (b) 한 번 회전
        for d in range(4):
            dx, dy = dirs[d]
            nd = cw[d]
            ndx, ndy = dirs[nd]
            for i in range(n):
                for j in range(m):
                    pre = B1[d][i][j]
                    if pre <= 0:
                        continue
                    # 회전 지점 (i,j)에서 소비한 마지막 값
                    last = last_sym_from_len(pre)
                    ns = next_sym(last)
                    qi, qj = i + ndx, j + ndy
                    post = 0
                    if 0 <= qi < n and 0 <= qj < m:
                        post = F[nd][ns][qi][qj]
                    total = pre + post
                    if total > ans:
                        ans = total

        return ans