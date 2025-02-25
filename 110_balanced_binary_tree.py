# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# took me about 13 minutes to solve. Didn't require extra study.
class Solution:
    def tree_depth(self, root):
        if root is None:
            return 0
        return 1 + max(self.tree_depth(root.left), self.tree_depth(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if not (root.left or root.right):
            return True
        
        if abs(self.tree_depth(root.left) - self.tree_depth(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

        