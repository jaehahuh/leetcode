class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch) + 1
        if idx == -1:
            return word
        
        return word[:idx][::-1] + word[idx:]