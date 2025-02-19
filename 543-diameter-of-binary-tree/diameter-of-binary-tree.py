# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        def dfs(node):
            if not node:
                return 0
            
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            # Update the diameter at this node
            self.longest = max(self.longest, left_depth + right_depth)
            
            # Return the depth of the current node
            return max(left_depth, right_depth) + 1
        
        dfs(root)
        return self.longest