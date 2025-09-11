class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        
        vowels_indices = [i for i, ch in enumerate(s) if ch in vowels]
        vowels_vals = sorted(s[i] for i in vowels_indices)

        list_s = list(s)
        for i, ch in zip(vowels_indices, vowels_vals):
            list_s[i] = ch

        return ''.join(list_s)