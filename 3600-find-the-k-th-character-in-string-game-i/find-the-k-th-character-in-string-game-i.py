class Solution:
    def kthCharacter(self, k: int) -> str:
        char_dict = {i:chr(ord('a') + i) for i in range(26)}
        word = 'a'

        while len(word) < k:
            generated_word = []
            for ch in word:
                generated_word.append(char_dict[(ord(ch) - ord('a') + 1) % 26])
            word += ''.join(generated_word)

        return word[k-1]