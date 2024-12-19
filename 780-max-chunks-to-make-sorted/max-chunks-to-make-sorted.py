class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        curr_max = -1
        max_chunks = 0
        for i, n in enumerate(arr):
            curr_max = max(n, curr_max)
            if curr_max == i:
                max_chunks += 1
    
        return max_chunks