class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Returns the total number of multiplication results (nums1[i] *nums2[j]) less than 
        # or equal to the given value.
        def count_total(value):
            count = 0
            for n1 in nums1:
                if n1 == 0: # 0 * num2[i] is always 0, so add len(nums2) to count
                    if value >= 0:
                        count += len(nums2)

                elif n1 > 0:
                    count += bisect.bisect_right(nums2, value/n1)
                
                else: # n1 < 0
                     count += len(nums2) - bisect.bisect_left(nums2, value/n1)
            return count
            
        low = -10**10 # -10^5 * 10^5 = -10^10
        high = 10**10 #  10^5 * 10^5 = -10^10

        result = high

        while low <= high:
            mid = low + (high - low)//2
            if count_total(mid) >= k:
                result = mid
                high = mid - 1
            else:
                low = mid + 1
    
        return result