class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        word_set = set(word)
        for ch in word_set:
            if ch.isupper() and ch.lower() in word_set:
                count += 1
        return count