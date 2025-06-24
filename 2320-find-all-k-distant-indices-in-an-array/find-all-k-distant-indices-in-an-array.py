class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result = []
        k_distant_indices = [False] * len(nums)

        for j in range(len(nums)):
            if nums[j] == key:
                start_i = max(0, j-k)
                end_i = min(len(nums)-1,j+k)

                for i in range(start_i, end_i + 1):
                    k_distant_indices[i] = True

        for i in range(len(nums)):
            if k_distant_indices[i]:
                result.append(i)

        return result