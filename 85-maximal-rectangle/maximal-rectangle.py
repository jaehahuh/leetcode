class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def rect_area(h):
            stack = []
            curr_max_area = 0
            h_extended = h + [0]
            
            for i in range(len(h_extended)):
                while stack and h_extended[stack[-1]] >= h_extended[i]:
                    height = h_extended[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    curr_max_area = max(curr_max_area, height * width)
                stack.append(i)
            return curr_max_area

        rows = len(matrix)
        cols = len(matrix[0])
        max_area = 0
        heights = [0] * cols

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0

            max_area = max(max_area, rect_area(heights))

        return max_area