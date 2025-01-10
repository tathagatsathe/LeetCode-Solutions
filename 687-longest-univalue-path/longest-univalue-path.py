# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def lup(root):
            l = 0
            r = 0
            nonlocal ans
            if(root==None):
                return 0
            if(root.left!=None):
                lf = lup(root.left)
            if(root.right!=None):
                rt = lup(root.right)
            if(root.left!=None and root.val == root.left.val):
                l = lf + 1
            if(root.right!=None and root.val == root.right.val):
                r = rt + 1

            ans = max(ans, l+r)
            # print(root.val, ans)
            return max(l,r)

        ans = max(lup(root), ans)

        return ans
        