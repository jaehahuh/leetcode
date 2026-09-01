class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        start_row, start_col = -1, -1
        litters = []

        # 시작점('S') 및 쓰레기('L') 위치 파악
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_row, start_col = r, c
                elif classroom[r][c] == 'L':
                    litters.append((r,c))

        litter_count = len(litters)
        target_mask = (1 << litter_count) - 1  # 모든 쓰레기를 전부 주운 상태 (bitmask)

        litter_map = {pos : i for i, pos in enumerate(litters)}
        
        max_energy = [[[-1] * (1 << litter_count) for _ in range(n)] for _ in range(m)] 
        
        q = deque([(0, start_row, start_col, 0, energy)]) # (moves, r, c, mask, curr_energy)
        max_energy[start_row][start_col][0] = energy

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            moves, r, c, mask, e = q.popleft()

            if mask == target_mask:
                return moves
            
            if e < max_energy[r][c][mask]:
                continue
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if classroom[nr][nc] == 'X':
                    continue
                
                next_energy = e - 1
                if next_energy < 0:
                    continue

                next_mask = mask
                cell = classroom[nr][nc]

                if cell == 'R':
                    next_energy = energy
                
                elif cell == 'L':
                    if (nr, nc) in litter_map:
                        next_mask |= (1 << litter_map[(nr,nc)])
                    
                if next_energy > max_energy[nr][nc][next_mask]:
                    max_energy[nr][nc][next_mask] = next_energy
                    q.append((moves + 1, nr, nc, next_mask, next_energy))

        return -1