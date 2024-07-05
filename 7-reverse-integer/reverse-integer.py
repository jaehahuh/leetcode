class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = x*(-1)
            num = (-1) * int(str((x))[::-1])
        else:
            num = int(str(x)[::-1])

        if num < -1*2**31 or num > 2**31 - 1 :
            return 0

        return num
        