class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -(2**31)   
        INT_MAX = (2**31)-1
        s = s.strip()
        sign = 1 #positive sign

        if len(s) == 0:
            return 0

        i = 0
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            i += 1

        num = 0
        while i < len(s):
            ch = s[i]
            if not ch.isdigit():
                break
            else:
                num = int(ch) + num*10
            i += 1

        num = sign * num

        if num < INT_MIN:
            return INT_MIN
        elif num > INT_MAX:
            return INT_MAX
        else:
            return num
    