class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Convert the list into a min-heap
        heapq.heapify(nums)
        op_count = 0

        while len(nums) > 1 and nums[0] < k:
            # Pop the two smallest elements from the heap
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)

            z = min(x,y) * 2 + max(x, y)
            heapq.heappush(nums, z)
            op_count += 1

        return op_count