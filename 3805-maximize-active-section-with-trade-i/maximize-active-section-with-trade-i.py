class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        new_s = '1' + s + '1'
        blocks = []
        i = 0
        n = len(new_s)

        while i < n:
            j = i
            while j < n and new_s[i] == new_s[j]:
                j += 1
            blocks.append((new_s[i], j-i))
            i = j
        
        base_ones = s.count('1')
        max_ones = base_ones

        for i in range(2,len(blocks)-2, 2):
            if blocks[i][0] == '1':
                left_zeros = blocks[i-1][1]
                middle_ones = blocks[i][1]
                right_zeros = blocks[i+1][1]

                other_ones = base_ones - middle_ones
                total_len = left_zeros + middle_ones + right_zeros
                max_ones = max(max_ones, total_len + other_ones)
        
        return max_ones