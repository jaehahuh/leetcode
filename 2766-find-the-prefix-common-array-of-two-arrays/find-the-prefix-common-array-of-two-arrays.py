class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        common = []
        set_A = set()
        set_B = set()

        for i in range(len(A)):
            set_A.add(A[i])
            set_B.add(B[i])

            count = len(set_A.intersection(set_B))
            common.append(count)
        
        return common