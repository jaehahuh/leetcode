class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[1], -x[0]))
        selected_points = []   
        rightmost = -10**18         # Largest selected point
        second_rightmost = -10**18  # Second largest selected point

        for start, end in intervals:
            count_in_interval = 0 # Count how many selected points fall in [start, end]
            if second_rightmost >= start and second_rightmost <= end:
                count_in_interval += 1
            if rightmost >= start and rightmost <= end:
                count_in_interval += 1
            
            if count_in_interval == 2:
                continue
            
            elif count_in_interval == 1:
                # add end to make two points
                selected_points.append(end)
                second_rightmost, rightmost = rightmost, end
            
            else: # count_in_interval == 0
                low_point = end - 1
                if low_point < start:
                    low_point = start
                selected_points.append(low_point)
                selected_points.append(end)
                second_rightmost, rightmost = low_point, end

        return len(selected_points)