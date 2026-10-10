class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        max_diff = 100000
        count = [0] * (max_diff + 2)
        n = len(nums1)
        k = k1 + k2

        for i in range(n):
            diff = abs(nums1[i] - nums2[i])
            count[diff] += 1

        diff_sum = sum(i * count[i] for i in range(max_diff + 1))
        if diff_sum <= k:
            return 0
        
        for d in range(max_diff, 0, -1):
            if count[d] > 0:
                reduce_count = min(k, count[d])
            
                count[d] -= reduce_count
                count[d-1] += reduce_count
                k -= reduce_count

                if k == 0:
                    break
    
        result = 0
        for d in range(max_diff + 1):
            if count[d] > 0:
                result += count[d] * (d * d)
        
        return result