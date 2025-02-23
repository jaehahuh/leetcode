# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Input validation
        if not preorder or not postorder or len(preorder) != len(postorder):
            return None

        n = len(postorder)
        post_val_to_idx = {n: i for i, n in enumerate(postorder)}  # Map postorder values to their indices

        def build(pre_start, pre_end, post_start):
            # Base case
            if pre_start > pre_end:
                return None
            
            root = TreeNode(preorder[pre_start])  # Create the current root node

            if pre_start != pre_end:  # If there is more than one node
                left_val = preorder[pre_start + 1]  # Value of the left child
                mid = post_val_to_idx[left_val]  # Index of the left child in postorder
                left_size = mid - post_start + 1  # Size of the left subtree

                # Recursively build the left and right subtrees
                root.left = build(pre_start + 1, pre_start + left_size, post_start)
                root.right = build(pre_start + left_size + 1, pre_end, mid + 1)

            return root
        
        return build(0, n - 1, 0)