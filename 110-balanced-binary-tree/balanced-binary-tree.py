# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        def fn(root):
            if root == None:
                return 0

            if root.left == None and root.right == None:
                return 1

            left_h = fn(root.left)
            right_h = fn(root.right)

            if left_h is False or right_h is False:
                return False

            if abs(left_h - right_h) <= 1:
                return 1 + max(left_h, right_h)

            return False
        
        res = fn(root)
        
        return bool(res) 