# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float("-inf")

        def maxPath(node):
            nonlocal ans

            if node == None:
                return 0

            l = max(maxPath(node.left),0)
            r = max(maxPath(node.right),0)
            ans = max(node.val+l+r, ans)

            return node.val +max(l,r)
            
        maxPath(root)

        return ans



        