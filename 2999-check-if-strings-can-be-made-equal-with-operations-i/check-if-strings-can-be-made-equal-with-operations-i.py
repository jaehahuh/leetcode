class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        even_s1 = sorted(s1[i] for i in range(0,4,2))
        even_s2 = sorted(s2[i] for i in range(0,4,2))
        odd_s1 = sorted(s1[i] for i in range(1,4,2))
        odd_s2 = sorted(s2[i] for i in range(1,4,2))
        return even_s1 == even_s2 and odd_s1 == odd_s2