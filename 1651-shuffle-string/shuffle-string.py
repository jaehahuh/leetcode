class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        suffled_string = ''
        dic = dict(zip(indices, s))
        sorted_dic = sorted(dic.items())
        for i in range(len(sorted_dic)):
            suffled_string += sorted_dic[i][1]
        
        return suffled_string