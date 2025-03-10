class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def count_at_least_k_consonants(k):
            vowel_count = defaultdict(int)  # Dictionary to store the count of vowels
            consonant_count = 0  # Count of consonants in the current window
            result = 0  # Count of valid substrings
            start = 0  # Starting index of the sliding window

            # Iterate through the string using the end pointer
            for end in range(len(word)):
                if word[end] in 'aeiou':
                    vowel_count[word[end]] += 1  
                else:
                    consonant_count += 1  

                # While all vowels are present and consonants are at least k
                while len(vowel_count) == 5 and consonant_count >= k:
                    # Add the count of substrings from current position to the end
                    result += (len(word) - end)

                    # Move the start pointer to maintain the condition
                    if word[start] in 'aeiou':
                        vowel_count[word[start]] -= 1  
                    else:
                        consonant_count -= 1 

                    # Remove the vowel from the dictionary if its count is zero
                    if vowel_count[word[start]] == 0:
                        del vowel_count[word[start]]
                    start += 1  
                    
            return result

        # Calculate the count of substrings with exactly k consonants
        return count_at_least_k_consonants(k) - count_at_least_k_consonants(k + 1)