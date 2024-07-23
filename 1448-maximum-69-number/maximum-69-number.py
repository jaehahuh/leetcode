class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        max_69 = ""
        for i in range(len(s)):
            if s[i] != "6":
                max_69 += s[i]
            else:
                max_69 += "9" + s[i+1:]
                return int(max_69)
        return int(max_69)