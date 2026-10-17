class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(n: int) -> int:
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total

        n = len(nums)
        arr = [(digit_sum(nums[i]), nums[i], i) for i in range(n)]
        
        arr.sort(key=lambda x: (x[0], x[1]))

        target_pos = [0] * n
        for new_idx, (_, _, orig_idx) in enumerate(arr):
            target_pos[orig_idx] = new_idx
            
        visited = [False] * n
        min_swaps = 0
        
        for i in range(n):
            if not visited[i] and target_pos[i] != i:
                cycle_size = 0
                curr = i
                while not visited[curr]:
                    visited[curr] = True
                    curr = target_pos[curr]
                    cycle_size += 1
                min_swaps += cycle_size - 1
                
        return min_swaps