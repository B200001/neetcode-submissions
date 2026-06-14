# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque()
        queue.append(root)
        rightmost = []

        while queue:
            l = len(queue)
            

            for i in range(l):
                node = queue.popleft()
                

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            rightmost.append(node.val)
            
        
        return rightmost