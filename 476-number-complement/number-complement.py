class Solution:
    def findComplement(self, num: int) -> int:
        comp = '0b'
        binary = bin(num)[2:]
        for i in binary:
            if i == '0':
                comp += '1'
            else:
                comp += '0'

        return int(comp, 2) #convert string binay to int