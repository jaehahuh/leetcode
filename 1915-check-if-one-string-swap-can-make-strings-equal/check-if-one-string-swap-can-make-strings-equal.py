class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        swap = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                swap.append((i, s2[i]))
        
        if len(swap) != 2:
            return False
        else:
            i1, char1 = swap[0]
            i2, char2 = swap[1]

        return s1[i1] == char2 and s1[i2] == char1