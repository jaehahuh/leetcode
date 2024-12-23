# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def count_swaps(nums_in_same_level):
            swaps = 0
            sorted_level = sorted(nums_in_same_level)

            hash_map = {num:index for index, num in enumerate(nums_in_same_level)}
            for i in range(len(nums_in_same_level)):
                if nums_in_same_level[i] != sorted_level[i]:
                    swaps += 1
                    #swap
                    j = hash_map[sorted_level[i]]
                    nums_in_same_level[i], nums_in_same_level[j] = nums_in_same_level[j], nums_in_same_level[i]
                    #update index after swap
                    hash_map[nums_in_same_level[i]] = i
                    hash_map[nums_in_same_level[j]] = j
            return swaps

        result = 0
        #BFS
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result += count_swaps(level)
        return result