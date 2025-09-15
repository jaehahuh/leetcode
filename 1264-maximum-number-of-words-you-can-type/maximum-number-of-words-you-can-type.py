class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count_cant_type = 0
        word_list = text.split(' ')
        letter_set = set(brokenLetters)
        for word in word_list:
            for letter in word:
                if letter in letter_set:
                    count_cant_type += 1
                    break
        
        return len(word_list) - count_cant_type