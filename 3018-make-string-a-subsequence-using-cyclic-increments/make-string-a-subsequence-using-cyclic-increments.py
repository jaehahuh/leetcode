class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        idx2 = 0  #index of str2
        
        for idx1 in range(len(str1)):
            if idx2 < len(str2):
                if str1[idx1] == str2[idx2]:
                    idx2 += 1
                elif (ord(str1[idx1])+1-ord('a'))%26 == (ord(str2[idx2])-ord('a'))%26:
                    idx2 += 1

        return idx2 == len(str2)