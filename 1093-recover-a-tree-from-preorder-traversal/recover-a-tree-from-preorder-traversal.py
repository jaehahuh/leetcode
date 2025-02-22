# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        i = 0

        while i < len(traversal):
            # Calculate the current depth
            depth = 0
            while i < len(traversal) and traversal[i] == '-':
                depth += 1
                i += 1
            
            # Extract node value
            value_start = i
            while i < len(traversal) and traversal[i].isdigit():
                i += 1
            val = int(traversal[value_start:i])
            node = TreeNode(val)

            # Find the parent node according to the current depth
            while len(stack) > depth:
                stack.pop()

            # Connect the child node to the parent node
            if stack:
                parent = stack[-1]
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node
                
            stack.append(node)
           
        return stack[0] # root node