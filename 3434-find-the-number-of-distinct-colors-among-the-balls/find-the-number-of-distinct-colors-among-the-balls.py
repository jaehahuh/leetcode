class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        distinct_colors = {}
        color_count = {} # Dictionary to count occurrences of each colo
        result = []

        for ball, color in queries:
            # If the ball already has a color, decrease the count of that color
            if ball in distinct_colors:
                previous_color = distinct_colors[ball]
                color_count[previous_color] -= 1
                if color_count[previous_color] == 0:
                    del color_count[previous_color]
                
            # Save the new color and add it to the set
            distinct_colors[ball] = color 
            # Increase the count of the new color
            if color in color_count:
                color_count[color] += 1
            else:
                color_count[color] = 1
                
            # Append the current number of distinct colors to the result
            result.append(len(color_count))
        
        return result