class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = sum(nums1), sum(nums2)
        sub = n2 - n1
        return int(sub/len(nums1))