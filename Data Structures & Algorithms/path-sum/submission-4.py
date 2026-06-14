# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum = 0
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        self.sum += root.val
        
        
        left = self.hasPathSum(root.left, targetSum)
        right = self.hasPathSum(root.right, targetSum)
        if self.sum == targetSum and not root.left and not root.right:
            return True

        self.sum -= root.val

        return left or right
        
