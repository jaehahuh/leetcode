class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        word_set = set(word)
        first_upper = {}
        last_lower = {}
        for i, ch in enumerate(word):
            if ch.islower():
                last_lower[ch] = i
            elif ch.isupper() and ch not in first_upper:
                first_upper[ch] = i

        for c in word_set:
            if c.islower() and c.upper() in word_set:
                if last_lower[c] < first_upper[c.upper()]:
                    count += 1
                
        return count