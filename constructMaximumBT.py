# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        index = nums.index(max(nums))
        return TreeNode(max(nums),self.constructMaximumBinaryTree(nums[:index]),
                        self.constructMaximumBinaryTree(nums[index+1:]))