class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        s1 = set(nums)
        s2 = set()
        
        s1_list = list(s1)
        n = len(s1_list)

        for i in range(n):
            for j in range(i, n):
                s2.add(s1_list[i] ^ s1_list[j])
        
        s3 = set()
        for val1 in s1:
            for va12 in s2:
                s3.add(val1 ^ va12)

        return len(s3)