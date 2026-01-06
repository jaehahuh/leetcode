# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = collections.deque([root])
        max_sum = float('-inf')
        max_sum_level = 1
        curr_level = 1

        while q:
            curr_level_sum = 0
            level_size = len(q)

            for _ in range(level_size):
                curr_node = q.popleft()
                curr_level_sum += curr_node.val

                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)

            if curr_level_sum > max_sum:
                max_sum = curr_level_sum
                max_sum_level = curr_level
        
            curr_level += 1
    
        return max_sum_level