""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    lowerBound = float("-inf")
    upperBound = float("inf")
    if lowerBound < root.data < upperBound:
        return Helper(root,lowerBound,upperBound)

def Helper(node,lwrBound,uprBound):
    if node:
        if lwrBound < node.data < uprBound:
            return Helper(node.left, lwrBound,node.data) and Helper(node.right, node.data,uprBound)
        else:
            return False
    return True
        