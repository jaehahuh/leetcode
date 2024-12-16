class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(num,index) for index, num in enumerate(nums)]
        heapq.heapify(heap)

        for _ in range(k):
            num, index = heapq.heappop(heap)
            nums[index] *= multiplier
            heapq.heappush(heap, (nums[index],index))

        return nums