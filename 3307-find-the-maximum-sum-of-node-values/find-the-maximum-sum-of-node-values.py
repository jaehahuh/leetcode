class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        xor_gains = [(num ^ k) - num for num in nums]  # Calculate gain from applying XOR with k for each node
        xor_gains.sort(reverse=True)
        max_sum = sum(nums)

        # Apply XOR in pairs (operation affects two nodes at once)
        for i in range(0, len(nums) - 1, 2):
            pair_gain = xor_gains[i] + xor_gains[i + 1]
            if pair_gain <= 0:
                break # Stop if no more gain
            max_sum += pair_gain
        
        return max_sum