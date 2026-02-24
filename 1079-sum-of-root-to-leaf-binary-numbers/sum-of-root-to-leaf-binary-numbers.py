# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def binaryToDecimal(binary):
            res = 0
            for i in range(len(binary)):
                res+=int(binary[i])*2**(len(binary) - i - 1)

            return res

        def fn(root):
            res = []
            if root == None:
                return []
            l = fn(root.left)
            r = fn(root.right)

            if l == [] and r == []:
                res = [str(root.val)]

            for i in l+r:
                res.append(str(root.val) + str(i))

            return res

        res = fn(root)
        ans = 0
        
        for r in res:
            ans+=binaryToDecimal(r)

        return ans
        
