class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        word_set = set(word)
        seen = set()
        ch_indices = defaultdict(list)
        for i, ch in enumerate(word):
            ch_indices[ch].append(i)
        for c in word_set:
            if c.islower() and c.upper() in word_set and c not in seen:
                if ch_indices[c][-1] < ch_indices[c.upper()][0]:
                    count += 1
                seen.add(c)
                
        return count