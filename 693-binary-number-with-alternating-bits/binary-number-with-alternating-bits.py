class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary_num = bin(n)[2:]
        for i in range(len(binary_num)-1):
            if binary_num[i] == binary_num[i+1]:
                return False
        return True