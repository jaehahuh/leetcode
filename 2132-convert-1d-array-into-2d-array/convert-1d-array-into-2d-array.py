class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res = []
        if m * n == len(original):
            for i in range(m):
                row = original[i * n : (i + 1) * n]
                res.append(row)
            return res
        else:
            return []