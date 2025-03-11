class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count_map = defaultdict(int) # Dictionary to count 'a, b, c'
        start = 0  # Start pointer for the sliding window
        result = 0
        for end in range(len(s)):
            count_map[s[end]] += 1

            while len(count_map) == 3:
                result += len(s) - end  # Count all substrings from start to the end of the string

                # Move the left pointer to shrink the window
                count_map[s[start]] -= 1
                if count_map[s[start]] == 0:
                    del count_map[s[start]] # Remove the character from the dictionary if count is zero
            
                start += 1

        return result # Total count of valid substrings