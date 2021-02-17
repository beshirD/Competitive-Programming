# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        res = []
        self.dfs(root,targetSum,0,res)
        return targetSum in res
    def dfs(self,node,target,summ,res):
        if not node.right and not node.left:
            res.append(summ + node.val)
        if node.left:
            self.dfs(node.left,target,summ + node.val,res)
        if node.right:
            self.dfs(node.right,target,summ + node.val,res)
            