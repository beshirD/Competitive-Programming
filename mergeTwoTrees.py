# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        root = TreeNode()
        if not root1 and not root2:
            return None
        elif not root1 and root2:
            root = root2
        elif root1 and not root2:
            root = root1
        elif root1 and root2:
            root.val = root1.val + root2.val
            root.left = self.mergeTrees(root1.left,root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
        return root