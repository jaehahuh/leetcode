# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #2^n, if n%2 == 1, then level is odd
        #e.g. 2^1 == 2, 2^3 == 8 ...
        #BFS 
        q = deque([root])
        level = 0
        while q:
            # check if the current level is odd
            if level%2 == 1: #or if level & 1:
                left, right = 0, len(q) - 1
                # reverse the values at the current odd level
                while left < right:
                    q[left].val, q[right].val = q[right].val, q[left].val
                    left += 1
                    right -= 1

            for _ in range(len(q)):
                curr_node = q.popleft()
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            level += 1

        return root