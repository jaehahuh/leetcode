# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return 0, None
            
            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)

            depth = max(left_depth, right_depth) + 1

            # If depths are equal, the current node is the LCA
            if left_depth == right_depth:
                return depth, node  
            
            # If the left subtree is deeper, return the left LCA
            if left_depth > right_depth:
                return depth, left_lca
            else: # If the right subtree is deeper, return the right LCA
                return depth, right_lca 
        
        depth, lca = dfs(root)
        return lca