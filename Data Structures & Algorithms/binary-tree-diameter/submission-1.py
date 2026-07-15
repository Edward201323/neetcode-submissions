# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.getDiameter(root)
        return self.diameter
        

    def getDiameter(self, root):
        if not root:
            return 0
        
        left = self.getDiameter(root.left)
        right = self.getDiameter(root.right)

        if left + right > self.diameter:
            self.diameter = left + right

        if left > right:
            return left + 1
        else:
            return right + 1