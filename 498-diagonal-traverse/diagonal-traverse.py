class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        result = []
        # 가능한 모든 대각선 인덱스 합: 0 ~ (rows-1)+(cols-1)
        for diag_sum in range(rows + cols - 1):
            # 현재 대각선에서 유효한 행 인덱스 범위 계산
            row_start = max(0, diag_sum - (cols - 1))
            row_end = min(rows - 1, diag_sum)

            # 짝수 대각선은 위로(행 감소), 홀수는 아래로(행 증가)
            if diag_sum % 2 == 0:
                row_iter = range(row_end, row_start - 1, -1)
            else:
                row_iter = range(row_start, row_end + 1)

            for row in row_iter:
                col = diag_sum - row
                result.append(mat[row][col])

        return result