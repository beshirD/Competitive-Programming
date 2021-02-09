# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        lower = float("-inf")
        upper = float("inf")
        return self.isValid(root,lower,upper)    
    
    
    
    def isValid(self,root,lower,upper):
        if(root != None):
            if(lower < root.val < upper):
                return self.isValid(root.left,lower,root.val) and self.isValid(root.right,root.val,upper)
            else:
                return False
        return True
        