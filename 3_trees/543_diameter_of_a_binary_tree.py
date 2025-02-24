# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestLine(self, root:Optional[TreeNode]) -> int:
        if root is None:
            return 0        
        return 1 + max(self.longestLine(root.left), self.longestLine(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        left = 0
        right = 0
        if root.left is not None:
            left = self.longestLine(root.left)
        if root.right is not None:
            right = self.longestLine(root.right)
        return max(left+right, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        
         