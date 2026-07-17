class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        freq = [0] * (max_val + 1)
        for num in nums:
            freq[num] += 1
        
        count = [0] * (max_val + 1)

        for g in range(max_val, 0, -1):
            total_multiples = 0
            for multiple in range(g, max_val + 1, g):
                total_multiples += freq[multiple]
            
            total_pairs = total_multiples * (total_multiples - 1) // 2

            for multiple in range(2 * g, max_val + 1, g):
                total_pairs -= count[multiple]
            
            count[g] = total_pairs
        
        prefix_sums = []
        distinct_gcds = []
        current_sum = 0

        for g in range(1, max_val + 1):
            if count[g] > 0:
                current_sum += count[g]
                prefix_sums.append(current_sum)
                distinct_gcds.append(g)
            
        answer = []
        for q in queries:
            idx = bisect.bisect_right(prefix_sums, q)
            answer.append(distinct_gcds[idx])
            
        return answer