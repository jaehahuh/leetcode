class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        lst = sentence.split(' ')
        for index, word in enumerate(lst):
            if word.startswith(searchWord):
                return index + 1
        return -1