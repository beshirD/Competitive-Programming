# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        total = [0]
        if root.left:
            self.dfs(root,root.left,total)
        if root.right:
            self.dfs(root,root.right,total)
        return total[0]
    def dfs(self,node,childNode,total):
        if childNode.left:
            if node.val % 2 == 0:
                total[0] +=  childNode.left.val
            self.dfs(childNode,childNode.left,total)
        if childNode.right:
            if node.val % 2 == 0:
                total[0] += childNode.right.val
            self.dfs(childNode,childNode.right,total)
        return total[0]
            
# BFS       
#         total = 0
#         queue = deque([(root,None,None)])
#         while queue:
#             node, parent,g_parent = queue.popleft()
#             if g_parent and (g_parent.val % 2 == 0):
#                 total += node.val
#             if node.left:
#                 queue.append((node.left,node,parent))
#             if node.right:
#                 queue.append((node.right,node,parent))
#         return total
        