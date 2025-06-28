class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        for i, n in enumerate(nums):
            heapq.heappush(min_heap, (n, i))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        top_k_elements = list(min_heap)
        top_k_elements.sort(key=lambda x:x[1])
        result = [element[0] for element in top_k_elements]

        return result