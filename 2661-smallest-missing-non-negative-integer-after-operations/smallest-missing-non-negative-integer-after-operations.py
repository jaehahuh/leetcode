class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mex = 0

        residue_freq = [0] * value
        for num in nums:
            residue = num % value
            residue_freq[residue] += 1
        
        while True:
            r = mex % value
            if residue_freq[r] > 0:
                residue_freq[r] -= 1
                mex += 1
            else:
                return mex