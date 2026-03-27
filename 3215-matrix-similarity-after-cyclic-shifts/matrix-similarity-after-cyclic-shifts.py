class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        for row in range(len(mat)):
            doubled_row = mat[row] + mat[row]
            n = len(mat[row])
            shift = k % n
            if row % 2 == 0:
                shifted_row = doubled_row[shift:shift + n]
            else:
                shifted_row = doubled_row[n-shift:n-shift+n]
            
            if shifted_row != mat[row]:
                return False
            
        return True