class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = 0
        count2 = 0
        #make nums list to set(hash table) for O(1) Time complexity 
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        for n1 in nums1:
            if n1 in set_nums2:
                count1 += 1
        for n2 in nums2:
            if n2 in set_nums1:
                count2 += 1
        
        return [count1, count2]