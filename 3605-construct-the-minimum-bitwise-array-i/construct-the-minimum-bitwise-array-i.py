class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            if num % 2 == 0:
                result.append(-1)
            else:
                for k in range(1, 32):
                    if ((num >> k) & 1) == 0:
                        ans = num ^ (1 << (k - 1))
                        result.append(ans)
                        break
                        
        return result