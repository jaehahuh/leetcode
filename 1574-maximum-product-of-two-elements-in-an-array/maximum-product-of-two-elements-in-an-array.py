class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, (-num))
        
        max_num1 = -heapq.heappop(max_heap)
        max_num2 = -heapq.heappop(max_heap)

        return (max_num1-1) * (max_num2-1)