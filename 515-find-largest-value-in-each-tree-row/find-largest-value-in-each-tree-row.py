# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        #BFS
        result = []
        if not root:
            return result
        
        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                curr_node = q.popleft()
                if curr_node:
                    level.append(curr_node.val)
                    if curr_node.left:
                        q.append(curr_node.left)
                    if curr_node.right:
                        q.append(curr_node.right)
            result.append(max(level))
        return result