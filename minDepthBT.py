# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        queue = deque()
        queue.append((root,1))
        
        while queue:
            node , level = queue.popleft()
            if not node.left and not node.right:
                return level
            
            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right,level+1))
                  
    #     if root == None:
    #         return 0
    #     return self.dfs(root)
    # def dfs(self,node):
    #     if self.isLeaf(node):
    #         return 1
    #     if node.left and node.right:
    #         left = self.dfs(node.left)
    #         right = self.dfs(node.right)
    #         return min(left,right) + 1
    #     if node.left:
    #         return self.dfs(node.left) + 1
    #     return self.dfs(node.right) + 1
    # def isLeaf(self,node):
    #     return not node.left and not node.right
    