class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
            
        vowels = 'aeiouAEIOU'
        count_vow = 0
        count_con = 0
        for ch in word:
            if not ch.isalnum():
                return False
            if ch.isalpha():
                if ch in vowels:
                    count_vow += 1
                else:
                    count_con += 1

        return count_vow >= 1 and count_con >= 1