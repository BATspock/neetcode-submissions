# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # do level order traversal 
        # add to answer the right most node
        if not root:
            return []
        dq = deque()
        ans = []
        dq.append(root)

        while len(dq) > 0:
            level_length = len(dq)
            level = []
            for i in range(len(dq)):
                node = dq.popleft()

                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)

                if i == level_length - 1:
                    ans.append(node.val)

            for l in level:
                dq.append(l)
        return ans

        