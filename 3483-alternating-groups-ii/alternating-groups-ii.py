class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        start = 0
        result = 0
        n = len(colors)

        # Loop through the colors array as a circular array
        for end in range(1, n + (k - 1)):
            # If the current tile and the previous tile have the same color, move start to the current end
            if colors[end % n] == colors[(end - 1) % n]:
                start = end
            
            # If the length of the sliding window exceeds k, move start forward
            if end - start + 1 > k:
                start += 1
                
            # If the length of the sliding window equals k, increment the result
            if end - start + 1 == k:
                result += 1
        
        return result