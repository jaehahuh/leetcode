class Solution:
    def makeFancyString(self, s: str) -> str:
        count = 1
        fancy_s = [s[0]]
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
                if count < 3:
                    fancy_s.append(s[i])
            else:
                count = 1
                fancy_s.append(s[i])
    
        return ''.join(fancy_s)