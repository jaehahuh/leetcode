class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_heap = []
        for i, num in enumerate(nums):
            # Using negative values allows the default min-heap to behave like a max-heap
            heapq.heappush(max_heap, (-num)) 
        
        element1 = -heapq.heappop(max_heap)
        element2 = -heapq.heappop(max_heap)
        
        return (element1-1) * (element2-1)