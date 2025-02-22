# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_length = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            # DFS recursive traversal to non-existing nodes
            left = dfs(node.left)
            right = dfs(node.right)

            # Add 1 to the length if the value of the current node is equal to the value of the child node
            left_path = left + 1 if node.left and node.left.val == node.val else 0
            right_path = right + 1 if node.right and node.right.val == node.val else 0

            # Compare result and left + right length
            self.max_length = max(self.max_length, left_path + right_path)

            # Return the largest of the child node's values
            return max(left_path, right_path)
        
        dfs(root)
        return self.max_length 