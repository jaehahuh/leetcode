class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n//2

        left_sum, right_sum = 0,0
        left_q, right_q = 0,0

        for i in range(mid):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])
        
        for i in range(mid, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])
        
        if (left_q + right_q) % 2 != 0:
            return True
        
        delta_sum = left_sum - right_sum
        delta_q = left_q - right_q

        return delta_sum * 2 != delta_q * -9