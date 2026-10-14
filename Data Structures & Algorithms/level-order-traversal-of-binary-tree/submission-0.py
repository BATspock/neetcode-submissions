# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        dq = deque()
        dq.append(root)

        while len(dq) > 0:
            level = []
            temp = []
            while len(dq) != 0:
                node = dq.popleft()
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
                level.append(node.val)
            for t in temp:
                dq.append(t)
            ans.append(level)

        return ans
