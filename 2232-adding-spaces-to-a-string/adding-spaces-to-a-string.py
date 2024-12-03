class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        pre_index = 0
        for index in spaces:
            res.append(s[pre_index:index] + ' ')
            pre_index = index
        res.append(s[pre_index:])
        return ''.join(res)