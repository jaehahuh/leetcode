class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        total = 0
        dic = {}

        #make hash map for each character of s and their corresponding indices
        for i, ch in enumerate(s):
            dic[ch] = i

        # Calculate the absolute difference between the index of the character in t 
        # and the index of the same character in s
        for i in range(len(t)):
            total += abs(dic[t[i]] - i)
        
        return total