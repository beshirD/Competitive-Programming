# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root):
        result = []
        queue = deque([(root,0)])
        currlevel = 1
        while queue:
            node, level = queue.popleft()
            if node:
                if level == currlevel:
                    if level % 2 == 0:
                        result[level].append(node.val)
                    else:
                        result[level].insert(0,node.val)
                else:
                    currlevel = level
                    result.append([node.val])

                if node.left:
                    queue.append((node.left,level + 1))
                if node.right:
                    queue.append((node.right,level + 1))
            
        return result
                
                
                    