class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        fixed_num = (tops[0],bottoms[0])
        result = float('inf')  # To store the minimum number of rotations

        for candidate in fixed_num:
            top_rotate = 0
            bottom_rotate = 0
            for i in range(len(tops)):
                if tops[i] != candidate and bottoms[i] != candidate:
                    break
                # If top doesn't match the candidate but bottom does, a top rotation is needed
                elif tops[i] != candidate:
                    top_rotate += 1
                # If bottom doesn't match the candidate but top does, a bottom rotation is needed
                elif bottoms[i] != candidate:
                    bottom_rotate += 1

            else:  # If loop completes without breaking, this target is valid
                result = min(result, top_rotate, bottom_rotate)

        # If no candidate was valid, return -1
        return result if result != float('inf') else -1 