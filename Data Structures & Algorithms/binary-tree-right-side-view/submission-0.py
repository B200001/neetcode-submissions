# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        level = 0

        queue = deque()
        
        queue.append(root)

        while queue:
            q_len = len(queue)
            rightSide = None

            for i in range(q_len):
                node = queue.popleft()

                if node:
                    rightSide = node
                    queue.append(node.left)
                    queue.append(node.right)
            if rightSide:
                res.append(rightSide.val)
            
        
        return res