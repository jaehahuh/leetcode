class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        count = [0] * 32
        for num in candidates:
            i = 0
            while num > 0:
                count[i] += 1 & num
                i += 1
                num = num >> 1
        return max(count)