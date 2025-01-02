class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = 'aeiou' # O(5)
        prefix_count = [0] * (len(words) + 1) # Initialize prefix count array
        count = 0 # counter for valid vowel strings

        # iterate through each word to count valid vowel strings
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                count += 1
            prefix_count[i+1] = count

        result = []
        # each query to find the number of valid vowel strings in the range
        for query in queries:
            start, end = query
            num_vowel_strings = prefix_count[end+1] - prefix_count[start]
            result.append(num_vowel_strings)

        return result