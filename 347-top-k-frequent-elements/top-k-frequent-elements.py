import heapq
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        heap = []

        for i in counter:
            # Since python heappush is stored in such a way that it obtains the minimum value,
            # I stores the value as a negative number and converts the maximum value to the minimum value.
            heapq.heappush(heap, (- counter[i] , i))

        top_k = list()
        for i in range(k):
            top_k.append(heapq.heappop(heap)[1])
    
        return top_k