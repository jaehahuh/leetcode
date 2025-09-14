class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = 'aeiou'
        def masking(word):
            word = word.lower()
            return ''.join('#' if ch in vowels else ch for ch in word)

        word_set = set(wordlist)
        case_map = {}
        vowel_map = {}

        for word in wordlist:
            word_lower = word.lower()
            mask_word = masking(word)
            if word_lower not in case_map:
                case_map[word_lower] = word
            if mask_word not in vowel_map:
                vowel_map[mask_word] = word
        
        result = []
        for q in queries:
            if q in word_set:
                result.append(q)
                continue
            word_lower = q.lower()
            if word_lower in case_map:
                result.append(case_map[word_lower])
                continue
            mask_word = masking(q)
            if mask_word in vowel_map:
                result.append(vowel_map[mask_word])
                continue
            result.append('')

        return result