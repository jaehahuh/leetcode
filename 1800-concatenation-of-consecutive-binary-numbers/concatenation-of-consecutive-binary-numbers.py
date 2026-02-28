class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        concat_num = ''
        for i in range(1,n+1):
            concat_num += bin(i)[2:]
        
        return int(concat_num,2)%MOD