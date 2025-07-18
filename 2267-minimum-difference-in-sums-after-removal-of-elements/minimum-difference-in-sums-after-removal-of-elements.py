class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        part_length = n//3

        # Left prefix sum using max-heap
        left_prefix_sum = [0] * (2*part_length)
        max_heap = []
        curr_sum = 0
        for i in range(part_length):
            heapq.heappush(max_heap, -nums[i]) # Max_heap
            curr_sum += nums[i]

        left_prefix_sum[part_length-1] = curr_sum 

        for i in range(part_length, 2 * part_length):
            heapq.heappush(max_heap, -nums[i])
            curr_sum += nums[i]
            curr_sum += heapq.heappop(max_heap)  # Subtract biggest one
            left_prefix_sum[i] = curr_sum

        # Right suffix sum using min-heap

        right_suffix_sum = [0] * (2 * part_length)
        min_heap = []
        curr_sum = sum(nums[2*part_length:])
        for num in nums[2*part_length:]:
            heapq.heappush(min_heap, num)
        right_suffix_sum[2 * part_length - 1] = curr_sum

        for i in range(2 * part_length - 1, part_length - 1, -1):
            heapq.heappush(min_heap, nums[i])
            curr_sum += nums[i]
            curr_sum -= heapq.heappop(min_heap)
            right_suffix_sum[i - 1] = curr_sum
        
        min_diff = float('inf')
        for i in range(part_length - 1, 2 * part_length):
            diff = left_prefix_sum[i] - right_suffix_sum[i]
            min_diff = min(min_diff, diff)

        return min_diff