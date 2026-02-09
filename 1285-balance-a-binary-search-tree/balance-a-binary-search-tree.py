# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        inorder_lst = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            inorder_lst.append(node.val)
            inorder(node.right)
        
        inorder(root)
        
        def bulid_balncedBST(left, right) -> Optional[TreeNode]:
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(inorder_lst[mid])
            root.left = bulid_balncedBST(left, mid-1)
            root.right = bulid_balncedBST(mid+1, right)

            return root
        
        return bulid_balncedBST(0, len(inorder_lst) - 1)