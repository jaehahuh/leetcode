class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        total_sum_of_areas = 0

        for x_coord, y_coord, side_length in squares:
            events.append((y_coord, side_length, True))
            events.append((y_coord + side_length, side_length, False))
            total_sum_of_areas += side_length * side_length

        target_half_area = total_sum_of_areas / 2

        events.sort()

        previous_y = 0
        accumulated_area = 0
        current_active_width = 0

        for current_y_event, side_length_of_square, is_start_event in events:
            height_segment = current_y_event - previous_y
            area_added_in_segment = height_segment * current_active_width
            accumulated_area_after_segment = accumulated_area + area_added_in_segment

            if accumulated_area_after_segment >= target_half_area:
                area_before_this_segment = accumulated_area
                remaining_area_to_target = target_half_area - area_before_this_segment
                total_area_of_this_segment = area_added_in_segment 
                
                if current_active_width > 0:
                    interpolation_ratio = remaining_area_to_target / total_area_of_this_segment
                    return previous_y + height_segment * interpolation_ratio
                else:
                    return previous_y

            accumulated_area = accumulated_area_after_segment

            if is_start_event:
                current_active_width += side_length_of_square
            else:
                current_active_width -= side_length_of_square
            
            previous_y = current_y_event
        return -1