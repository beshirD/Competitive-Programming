# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:  
        if preorder:
            root = TreeNode(preorder[0])
            leftArray = []
            rightArray = []
            for i in preorder:
                if i < preorder[0]:
                    leftArray.append(i)
                elif i > preorder[0]:
                    rightArray.append(i)
                    
          
            if len(leftArray) == 0:
                root.left = None
            if len(rightArray) == 0:
                root.right = None
            
            root.left = self.bstFromPreorder(leftArray)
            root.right = self.bstFromPreorder(rightArray)
            return root