class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter = Counter(words)
        palin_length = 0

        for word in list(counter.keys()):
            reversed_word = word[::-1]
            if word == reversed_word: # 'aa', 'bb' 
                pair = counter[word] // 2
                palin_length += pair * 4
                counter[word] -= pair * 2
            
            else: # "ab" , "ba"
                if reversed_word in counter:
                    pair = min(counter[word], counter[reversed_word])
                    palin_length += pair * 4
                    counter[word] -= pair
                    counter[reversed_word] -= pair

            # If there is any remaining palindromic word, place one in the center
        for word in counter:
            if word[0] == word[1] and counter[word] > 0:
                palin_length += 2
                break
            
        return palin_length