# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def rob_f(node):
            if node == None:
                return [0,0]

            l = rob_f(node.left)
            r = rob_f(node.right)

            rb = l[1] + r[1] + node.val
            nrb = max(l) + max(r)

            return [rb, nrb]

        return max(rob_f(root))
        