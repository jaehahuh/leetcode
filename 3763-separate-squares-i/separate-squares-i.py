class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0
        min_y = float('inf')
        max_y_plus_l = float('-inf')

        for x, y, l in squares:
            total_area += l * l
            min_y = min(min_y, y)
            max_y_plus_l = max(max_y_plus_l, y + l)
        
        target_area = total_area / 2

        def get_area_below(y_line_coord):
            current_area = 0
            for x, y, l in squares:
                bottom = y
                top = y + l
                
                if top <= y_line_coord:
                    current_area += l * l
                elif bottom < y_line_coord < top:
                    current_area += l * (y_line_coord - bottom)
            return current_area

        low = min_y
        high = max_y_plus_l
        
        for _ in range(100): 
            mid_y = (low + high) / 2
            area_below_mid = get_area_below(mid_y)

            if area_below_mid < target_area:
                low = mid_y
            else:
                high = mid_y
                
        return high