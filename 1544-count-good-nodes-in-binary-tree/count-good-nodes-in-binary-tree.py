# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        def dfs(root, parent):
            nonlocal ans

            if root == None:
                return

            if root.val >= parent:
                ans+=1

            max_ = max(root.val, parent)
            dfs(root.left, max_)
            dfs(root.right, max_)

        dfs(root, -10**5)

        return ans