class Solution:
    def maxFreqSum(self, s: str) -> int:
        count_dict = Counter(s)
        vowels = {'a', 'e', 'i', 'o', 'u'} 
        max_vowel = 0 
        max_consonant = 0 

        for ch, count in count_dict.items(): 
            if ch in vowels: 
                if count > max_vowel: 
                    max_vowel = count

        for ch, count in count_dict.items():
            if ch not in vowels:
                if count > max_consonant:
                    max_consonant = count
        
        return max_vowel + max_consonant