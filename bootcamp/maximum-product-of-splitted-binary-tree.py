# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root) -> int:

        def calculate_total_sum(node):
            total = node.val
            if not node.left and not node.right:
                return node.val
            if node.left:
                total += calculate_total_sum(node.left)
            if node.right:
                total += calculate_total_sum(node.right)
            return total
         
        def calculate_max_product(node,total_sum):
            left_subtree_sum = 0
            right_subtree_sum = 0
            max_product = 0
            total = 0
            if not node.left and not node.right:
                return (total_sum - node.val) * node.val, node.val
            
            if node.left:
                
                left_max_product, left_subtree_sum = calculate_max_product(node.left,total_sum)
 
                max_product  = max(max_product, left_max_product)

          
            if node.right:
                right_max_product, right_subtree_sum = calculate_max_product(node.right,total_sum)

                max_product  = max(max_product, right_max_product)

            
            total = left_subtree_sum + right_subtree_sum + node.val
            max_product = max(max_product, total * (total_sum - total))

          
            return max_product, total
            
        # max_product, sum
        
        total =  calculate_total_sum(root)
        res = calculate_max_product(root,total)
        return res[0] % (10**9 + 7)