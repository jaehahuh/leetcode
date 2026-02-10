class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0

        for start in range(n):
            even_count = defaultdict(int)
            odd_count = defaultdict(int)
            even_distinct = 0
            odd_distinct = 0

            for end in range(start, n):
                num = nums[end]
                if num % 2 == 0:
                    if even_count[num] == 0:
                         even_distinct += 1
                    even_count[num] += 1
                else:
                    if odd_count[num] == 0:
                        odd_distinct += 1
                    odd_count[num] += 1
            
                if even_distinct == odd_distinct:
                    max_len = max(max_len, end - start + 1)
        
        return max_len