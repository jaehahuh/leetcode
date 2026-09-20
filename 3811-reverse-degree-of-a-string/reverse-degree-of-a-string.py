class Solution:
    def reverseDegree(self, s: str) -> int:
        rev_degree = 0
        rev_alphabets = {}
        j = 0
        for i in range(26, 0, -1):
            rev_alphabets[chr(ord('a')+j)] = i
            j += 1
        for idx, ch in enumerate(s):
            rev_degree += rev_alphabets[ch] * (idx + 1)

        return rev_degree