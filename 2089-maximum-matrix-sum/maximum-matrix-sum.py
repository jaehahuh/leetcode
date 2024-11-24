class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        result = 0
        neg_count = 0
        matrix_min = float("inf")
        for row in matrix:
            for n in row:
                result += abs(n)
                matrix_min = min(matrix_min, abs(n))
                if n < 0:
                    neg_count += 1
        
        if neg_count & 1:
            result -= 2 * matrix_min
        
        return result