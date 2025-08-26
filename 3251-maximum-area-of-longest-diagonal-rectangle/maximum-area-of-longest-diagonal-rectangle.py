class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_area = 0
        longest_dia = 0
        for l, w in dimensions:
            dia = l**2 + w**2
            area = l * w
            if dia > longest_dia:
                longest_dia = dia
                max_area = area
            elif dia == longest_dia and area > max_area:
                max_area = area
                
        return max_area 