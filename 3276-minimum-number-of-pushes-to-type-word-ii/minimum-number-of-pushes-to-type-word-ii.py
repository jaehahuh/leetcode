class Solution:
    def minimumPushes(self, word: str) -> int:
        word_counts = Counter(word)
        sorted_word = [char * count for char, count in word_counts.most_common()]
        new_word = ''.join(sorted_word)

        n = len(new_word)
        count_dict = defaultdict(int)
        result = 0
        for i in range(n):
            if new_word[i] not in count_dict:
                length = len(count_dict)
                count_dict[new_word[i]] = (length//8) + 1
                result += (length//8) + 1
            else:
                result += count_dict[new_word[i]]
        
        return result