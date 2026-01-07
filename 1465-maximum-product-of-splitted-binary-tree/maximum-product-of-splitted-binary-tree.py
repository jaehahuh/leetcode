# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
    
        def calculate_tree_sum(node):
            if not node:
                return 0
            return node.val + calculate_tree_sum(node.left) + calculate_tree_sum(node.right)

        total_tree_sum = calculate_tree_sum(root)
        self.max_product = 0

        def dfs(node): # Find max product
            if not node:
                return 0

            left_subtree_sum = dfs(node.left)
            right_subtree_sum = dfs(node.right)

            curr_subtree_sum = node.val + left_subtree_sum + right_subtree_sum
            curr_product = curr_subtree_sum * (total_tree_sum - curr_subtree_sum)

            self.max_product = max(self.max_product, curr_product)
            return curr_subtree_sum
        
        dfs(root)
        return self.max_product % MOD