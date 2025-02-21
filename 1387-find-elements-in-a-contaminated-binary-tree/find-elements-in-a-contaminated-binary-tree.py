# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.values = set() # Store the recovered values

        def recover(node, x):
            if node == None:
                return 
            
            node.val = x
            self.values.add(x) # Add the recovered value to the set

            # Change the values for the left and right child nodes
            recover(node.left, 2* x + 1)
            recover(node.right, 2 * x + 2)

        recover(root, 0)  # Start recovery with the root value set to 0

    def find(self, target: int) -> bool:
        return True if target in self.values else False # Check if the target exists in the set


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)