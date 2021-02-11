# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        nums = []
        result = self.app(root,nums)
        min = 10 ** 5
        for i in range(1,len(result)):
            x = result[i] - result[i-1]
            if x < min:
                min = x
        return min
                    
    def app(self,root,nums):
        if root != None:

            self.app(root.left,nums)
            nums.append(root.val)
            self.app(root.right,nums)
        return nums
            
        
            
            
        