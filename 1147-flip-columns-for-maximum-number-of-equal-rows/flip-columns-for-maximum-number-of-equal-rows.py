class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = collections.defaultdict(int)

        for row in matrix:
            row_key = str(row)
            if row[0]:
                row_key = str([0 if n else 1 for n in row])
            count[row_key] += 1

        return max(count.values())