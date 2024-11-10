# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#BFS solution
from collections import deque

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = collections.deque([root])
        deepest_leaves_sum = 0

        while queue:
            level_sum = 0 #initialize level sum
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val  # add current node's value in current level_sum 

                # add children node in queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            #update the sum of current level to deepest node sum
            deepest_leaves_sum = level_sum
            
        return deepest_leaves_sum