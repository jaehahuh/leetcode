# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        # check if the current node is the start of a valid path
        if self.dfs(head, root):
            return True
        # otherwise, check the left and right subtrees
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def dfs(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        
        if not root or head.val != root.val:
            return False
        
        return self.dfs(head.next, root.left) or self.dfs(head.next, root.right)