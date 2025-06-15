class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)

        for ch in s:
            if ch != '9':
                a = int(s.replace(ch, '9'))
                break
        else:
            a = num
        
        if s[0] != '1':
            b = int(s.replace(s[0], '1'))
        else:
            for ch in s[1:]:
                if ch != '0' and ch != '1':
                    b = int(s.replace(ch, '0'))
                    break
            else:
                b = num

        return a - b