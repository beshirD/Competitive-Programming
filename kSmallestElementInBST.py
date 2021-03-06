# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        result = []
        self.inOrder(root,result)
        for index in range(k):
            kSmallest = result[index]
            
        return kSmallest
    def inOrder(self,node,result):
        if node:
            self.inOrder(node.left,result)
            result.append(node.val)
            self.inOrder(node.right,result)
        return result
        