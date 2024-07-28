class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(32): # iterate each bit position from 0 to 31 (32bits for integer)
            count = 0
            for num in nums:
                if num & (1 << i):
                    count += 1
            if count >= k:
                ans |= (1 << i)
        return ans