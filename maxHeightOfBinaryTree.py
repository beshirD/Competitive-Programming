from collections import deque
def height(root):
    max_height = 0
    if not root:
        return 0
    if not root.left and not root.right:
        return 0
    if root.left:
        max_height = max(max_height,height(root.left))
    if root.right:
        max_height = max(max_height,height(root.right)) 
    return max_height + 1
    
        
    
    # queue = deque([(root,0)])
    # while queue:
    #     node , level = queue.popleft()
    #     if node.left:
    #         queue.append((node.left,level + 1))
    #     if node.right:
    #         queue.append((node.right,level + 1))
    # return level


