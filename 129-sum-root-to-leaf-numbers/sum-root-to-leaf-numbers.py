# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def fn(root):
            if root == None:
                return []

            l = fn(root.left)
            r = fn(root.right)

            res = []
            for i in range(len(l)):
                res.append(str(root.val) + str(l[i]))
            for i in range(len(r)):
                res.append(str(root.val) + str(r[i]))
            if res == []:
                res = [str(root.val)]

            return res

        res = fn(root)

        ans = 0

        for r in res:
            ans+=int(r)

        return ans