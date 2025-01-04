class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        palin_subseq = set() # (mid_character, outer_character)  e.g) o m o 
        left = set()
        right = collections.Counter(s)

        for mid_char in s:
            right[mid_char] -= 1
            for outer_char in left:
                if right[outer_char] > 0:  # ensure outer character still exists
                    palin_subseq.add((mid_char, outer_char)) # add to palindromic subsequences
            left.add(mid_char)

        return len(palin_subseq)