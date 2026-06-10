class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        max_log = n.bit_length() 
        max_table = [[0] * max_log for _ in range(n)]
        min_table = [[0] * max_log for _ in range(n)]

        for i in range(n):
            max_table[i][0] = nums[i]
            min_table[i][0] = nums[i]

        for j in range(1, max_log):
            jump = 1 << (j - 1) 
            for i in range(n - (1 << j) + 1):
                max_table[i][j] = max(max_table[i][j - 1], max_table[i + jump][j - 1])
                min_table[i][j] = min(min_table[i][j - 1], min_table[i + jump][j - 1])


        def get_max(left: int, right: int) -> int:
            j = (right - left + 1).bit_length() - 1
            return max(max_table[left][j], max_table[right - (1 << j) + 1][j])

        def get_min(left: int, right: int) -> int:
            j = (right - left + 1).bit_length() - 1
            return min(min_table[left][j], min_table[right - (1 << j) + 1][j])

        max_heap = []
        for left in range(n):
            right = n - 1
            subarray_value = get_max(left, right) - get_min(left, right)
            max_heap.append((-subarray_value, left, right))
        
        heapq.heapify(max_heap)

        total_value = 0
        
        for _ in range(k):
            neg_value, left, right = heapq.heappop(max_heap)
            total_value -= neg_value 

            if right > left:
                next_right = right - 1
                next_value = get_max(left, next_right) - get_min(left, next_right)
                heapq.heappush(max_heap, (-next_value, left, next_right))
                
        return total_value