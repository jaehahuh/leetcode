class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words_map = collections.Counter(words)
        # All the strings of words are of the same length.
        word_length = len(words[0])
        word_count = len(words)
        total_length = word_length * word_count

        result = []
        # use sliding window
        for i in range(len(s)-total_length+1):
            seen_words = {}
            for j in range(word_count):
                start_index = i + j * word_length
                word = s[start_index : start_index + word_length]

                if word in words_map:
                    if word in seen_words:
                        seen_words[word] += 1
                    else:
                        seen_words[word] = 1

                    # If the current word count exceeds the words array count
                    if seen_words[word] > words_map[word]:
                        break
                else:
                    break
            else:
                # If all words match, append the index to the result.
                result.append(i)

        return result