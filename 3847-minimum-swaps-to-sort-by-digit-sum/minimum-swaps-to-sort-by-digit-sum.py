class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        digits = []
        for i, num in enumerate(nums):
            digit_sum = 0
            temp = num
            while temp > 0:
                digit_sum += temp%10
                temp //= 10
            digits.append((digit_sum, num, i))
        
        sorted_digits = sorted(digits, key=lambda x: (x[0],x[1]))
        digits_pos = [i for digits_sum, num, i in sorted_digits]
        
        n = len(nums)
        index_pos = sorted(enumerate(digits_pos), key=lambda x: x[1])
        visited = [False] * n
        
        min_swaps = 0
        for i in range(n):
            if visited[i] or index_pos[i][0] == i:
                continue
            
            cycle_size = 0
            curr = i

            while not visited[curr]:
                visited[curr] = True
                curr = index_pos[curr][0]
                cycle_size += 1

            if cycle_size > 1:
                min_swaps += (cycle_size - 1)
        
        return min_swaps