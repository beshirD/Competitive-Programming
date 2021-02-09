# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        sum = 0
        if root == None:
            return sum 
        elif low <= root.val <= high:
            sum += root.val
            sum += self.rangeSumBST(root.left,low,high)
            sum += self.rangeSumBST(root.right,low,high)
            return sum
        else:
            sum += self.rangeSumBST(root.left,low,high)
            sum += self.rangeSumBST(root.right,low,high)
            return sum
        
        