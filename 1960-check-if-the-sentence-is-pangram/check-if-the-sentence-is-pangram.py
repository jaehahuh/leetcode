class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        unique_chars = set(sentence)
        return len(unique_chars) == 26