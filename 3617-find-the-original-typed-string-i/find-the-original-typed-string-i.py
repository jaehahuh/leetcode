class Solution:
    def possibleStringCount(self, word: str) -> int:
        total_possible_strings = 1 # Case: where no clumsy typing occurred (word itself)

        i = 0
        while i < len(word):
            curr_char = word[i]
            length_char = 0
            j = i
            # Find the length of the current consecutive char
            while j < len(word) and word[j] == curr_char:
                length_char += 1
                j += 1

            total_possible_strings += (length_char - 1)
            i = j # Move to the start of the next char
        
        return total_possible_strings   