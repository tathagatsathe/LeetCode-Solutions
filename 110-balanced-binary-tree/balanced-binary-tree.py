# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None :
            return True

        def checkDepth(root):
            if root == None:
                return 0
            d1 = checkDepth(root.left)
            d2 = checkDepth(root.right)

            if (type(d1) == bool or type(d2) == bool) or abs(d1-d2)>1:
                return False

            return 1 + max(d1,d2)

        d = checkDepth(root)

        return bool(d)
