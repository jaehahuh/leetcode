class Solution:
    def binaryGap(self, n: int) -> int:
        binary_num = bin(n)[2:]
        prev_i = -1
        longest_distance = 0
        for i in range(len(binary_num)):
            cuur_distance = 0
            if binary_num[i] == '1' and prev_i == -1:
                prev_i = i
            elif binary_num[i] == '1' and prev_i != -1:
                curr_distance = i - prev_i
                longest_distance = max(longest_distance, curr_distance)
                prev_i = i
        
        return longest_distance