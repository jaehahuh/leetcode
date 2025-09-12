class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set('aeiou')
        return any(ch in vowels for ch in s)