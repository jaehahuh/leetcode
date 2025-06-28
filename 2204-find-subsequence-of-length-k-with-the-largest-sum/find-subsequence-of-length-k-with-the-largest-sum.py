class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        index_list = [(n, i) for i, n in enumerate(nums)]
        index_list.sort(key=lambda x:x[0], reverse=True)
        top_k_elements = index_list[:k]
        top_k_elements.sort(key=lambda x:x[1])
        result = [element[0] for element in top_k_elements]

        return result