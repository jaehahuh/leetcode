class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for ch in sorted(set(s)):
            suffix = s[s.index(ch):]
            #set은 순서 상관 x, unique한 값
            if set(s) == set(suffix):
                return ch + self.removeDuplicateLetters(suffix.replace(ch,''))
        return ''