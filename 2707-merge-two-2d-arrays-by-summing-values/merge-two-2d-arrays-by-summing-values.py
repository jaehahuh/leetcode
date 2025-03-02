class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        hash_map = defaultdict(int)
        result = []

        for index, num in nums1:
            hash_map[index] += num
        
        for index, num in nums2:
            hash_map[index] += num
        
        result = sorted(hash_map.items())
        
        return result