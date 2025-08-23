class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        ones_coords = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    ones_coords.append((r, c))

        def get_min_rect_area(r_start, r_end, c_start, c_end) -> int:
            min_r, max_r = float('inf'), float('-inf')
            min_c, max_c = float('inf'), float('-inf')

            found_one = False

            for r, c in ones_coords:
                if r_start <= r <= r_end and c_start <= c <= c_end:
                    min_r = min(min_r, r)
                    max_r = max(max_r, r)
                    min_c = min(min_c, c)
                    max_c = max(max_c, c)
                    found_one = True
            
            if not found_one:
                return 0
            
            return (max_r - min_r + 1) * (max_c - min_c + 1)

        min_total_area = float('inf')

        for r1 in range(rows - 2): 
            for r2 in range(r1 + 1, rows - 1): # 두
                area1 = get_min_rect_area(0, r1, 0, cols - 1)
                area2 = get_min_rect_area(r1 + 1, r2, 0, cols - 1)
                area3 = get_min_rect_area(r2 + 1, rows - 1, 0, cols - 1)
                
                if area1 > 0 and area2 > 0 and area3 > 0:
                    min_total_area = min(min_total_area, area1 + area2 + area3)

        for c1 in range(cols - 2):
            for c2 in range(c1 + 1, cols - 1): 
                area1 = get_min_rect_area(0, rows - 1, 0, c1)
                area2 = get_min_rect_area(0, rows - 1, c1 + 1, c2)
                area3 = get_min_rect_area(0, rows - 1, c2 + 1, cols - 1)
                
                if area1 > 0 and area2 > 0 and area3 > 0:
                    min_total_area = min(min_total_area, area1 + area2 + area3)
            
        for r_cut in range(rows - 1): 
            area_top = get_min_rect_area(0, r_cut, 0, cols - 1)
            if area_top == 0: 
                continue 

            for c_split in range(cols - 1): 
                area_bottom_left = get_min_rect_area(r_cut + 1, rows - 1, 0, c_split)
                area_bottom_right = get_min_rect_area(r_cut + 1, rows - 1, c_split + 1, cols - 1)
                
                if area_bottom_left > 0 and area_bottom_right > 0:
                    min_total_area = min(min_total_area, area_top + area_bottom_left + area_bottom_right)
            
        for r_cut in range(rows - 1):
            area_bottom = get_min_rect_area(r_cut + 1, rows - 1, 0, cols - 1)
            if area_bottom == 0: 
                continue
            
            for c_split in range(cols - 1): 
                area_top_left = get_min_rect_area(0, r_cut, 0, c_split)
                area_top_right = get_min_rect_area(0, r_cut, c_split + 1, cols - 1)
                
                if area_top_left > 0 and area_top_right > 0:
                    min_total_area = min(min_total_area, area_bottom + area_top_left + area_top_right)

        for c_cut in range(cols - 1):
            area_left = get_min_rect_area(0, rows - 1, 0, c_cut)
            if area_left == 0: 
                continue

            for r_split in range(rows - 1): 
                area_right_top = get_min_rect_area(0, r_split, c_cut + 1, cols - 1)
                area_right_bottom = get_min_rect_area(r_split + 1, rows - 1, c_cut + 1, cols - 1)
                
                if area_right_top > 0 and area_right_bottom > 0:
                    min_total_area = min(min_total_area, area_left + area_right_top + area_right_bottom)

        for c_cut in range(cols - 1): 
            area_right = get_min_rect_area(0, rows - 1, c_cut + 1, cols - 1)  
            if area_right == 0: 
                continue

            for r_split in range(rows - 1): 
                area_left_top = get_min_rect_area(0, r_split, 0, c_cut)
                area_left_bottom = get_min_rect_area(r_split + 1, rows - 1, 0, c_cut)
                
                if area_left_top > 0 and area_left_bottom > 0:
                    min_total_area = min(min_total_area, area_right + area_left_top + area_left_bottom)
        

        return min_total_area