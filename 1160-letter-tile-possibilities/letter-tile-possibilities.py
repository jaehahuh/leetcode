class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles) #char -> available count
       
        def backtrack():
            possible_seq = 0
            for ch in count:
                if count[ch] > 0:
                    count[ch] -= 1  # Select the current character
                    possible_seq += 1  # Add the sequence formed by the current character
                    possible_seq += backtrack()   # Recursive call
                    count[ch] += 1  # Unselect the current character
            return possible_seq 

        return backtrack()  # Return the count of non-empty sequences