class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        negative_count = 0
        matrix_min = float('inf')
        
        for r in matrix:
            for n in r:
                if n < 0:
                    negative_count += 1
                total_sum += abs(n)
                matrix_min = min(matrix_min, abs(n))
        
        if negative_count % 2 != 0:
            return total_sum - (2*matrix_min)
        
        return total_sum