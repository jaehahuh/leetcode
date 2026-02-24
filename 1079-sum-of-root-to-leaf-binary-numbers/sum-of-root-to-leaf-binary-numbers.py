# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path, all_paths):
            if node is None:
                return
            path.append(node.val)

            if node.left is None and node.right is None:
                all_paths.append(list(path))
            else:
                dfs(node.left, path, all_paths)
                dfs(node.right, path, all_paths)
 
            path.pop()
        
        all_paths = []
        dfs(root, [], all_paths)
        total = 0
        for path in all_paths:
            binary_num = ''.join(str(bit) for bit in path)
            decimal_num = int(binary_num, 2)
            total += decimal_num
                
        return total