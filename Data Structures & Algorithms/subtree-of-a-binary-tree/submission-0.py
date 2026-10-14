# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False

        def helper(root, sub_root):
            if not root and not sub_root:
                return True

            elif root and not sub_root:
                return False
            
            elif not root and sub_root:
                return False

            elif root.val != sub_root.val:
                return False
            
            return helper(root.left, sub_root.left) and helper(root.right, sub_root.right)

        def dfs(root):
            
            if not root:
                return False

            res = False

            if root.val == subRoot.val:
                res = helper(root, subRoot)

            if res:
                return True

            in_left =  dfs(root.left) 
            in_right =  dfs(root.right)

            return in_left or in_right

        return dfs(root)