class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0

        # If the length of nums1 is odd
        if len(nums1) % 2 == 1:
            for num in nums2: # XOR all elements of nums2 and add to the result
                result ^= num

         # If the length of nums2 is odd
        if len(nums2) % 2 == 1:
            for num in nums1: # XOR all elements of nums1 and add to the result
                result ^= num

        return result