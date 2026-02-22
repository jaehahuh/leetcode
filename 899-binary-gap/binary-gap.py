class Solution:
    def binaryGap(self, n: int) -> int:
        binary_num = bin(n)[2:]
        positions = [i for i, bit in enumerate(binary_num) if bit == '1']
        longest_distance = 0
        for i in range(1, len(positions)):
            longest_distance = max(longest_distance, positions[i]-positions[i-1])
        return longest_distance