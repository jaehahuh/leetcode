class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        for s in sentences:
            words = s.split(' ')
            max_words = max(max_words, len(words))
        return max_words