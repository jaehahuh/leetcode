class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        index_arr = sorted((num, index) for index, num in enumerate(nums))
        result = [0] * n

        i = 0
        while i < n:
            j = i + 1
            while j < n and index_arr[j][0] - index_arr[j-1][0] <= limit:
                j += 1
            
            indices = sorted(index_arr[k][1] for k in range(i, j))

            for k in range(i, j):
                result[indices[k-i]] = index_arr[k][0]
            
            i = j
        
        return result