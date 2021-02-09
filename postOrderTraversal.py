# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.postOrd(root,result)
        return result
    
    
    def postOrd(self,root,result):
        if root != None:
            self.postOrd(root.left,result)
            self.postOrd(root.right,result)
            result.append(root.val)
            
            