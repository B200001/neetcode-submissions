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
        
        # if self.sum == targetSum and not root.left and not root.right:
        #     return True
        left = self.hasPathSum(root.left, targetSum)
        if self.sum == targetSum and not root.left and not root.right:
            return True
        right = self.hasPathSum(root.right, targetSum)
        

        self.sum -= root.val

        return left or right
        
