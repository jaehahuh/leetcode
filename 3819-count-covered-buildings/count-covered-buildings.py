class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rows = defaultdict(list) # x : y
        cols = defaultdict(list) # y: x
        for r, c in buildings:
            rows[r].append(c)
            cols[c].append(r)

        min_y_in_row = {r: min(coords) for r, coords in rows.items()}
        max_y_in_row = {r: max(coords) for r, coords in rows.items()}
        min_x_in_col = {c: min(coords) for c, coords in cols.items()}
        max_x_in_col = {c: max(coords) for c, coords in cols.items()}
        
        covered_count = 0
        for r, c in buildings:
            is_covered = True
            if min_x_in_col[c] >= r:
                is_covered = False
            if max_x_in_col[c] <= r:
                is_covered = False
            if min_y_in_row[r] >= c:
                is_covered = False
            if max_y_in_row[r] <= c:
                is_covered = False
            
            if is_covered:
                covered_count += 1
                
        return covered_count