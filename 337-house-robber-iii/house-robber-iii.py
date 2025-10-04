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

            # d0 = l[1] + r[1]
            # d1 = l[1] + r[1] + node.val
            # d2 = l[1] + r[0]
            # d3 = l[0] + r[1]
            # d4 = l[0] + r[0]

            # temp = [d1, d4]
            # if d2>d1 and d2>d3 and d2>d4:
            #     temp = [d1, d2]
            # elif d3>d1 and d3>d2 and d3>d4:
            #     temp = [d1, d3]
            # elif d0>d4:
            #     temp[1] = d0

            # return temp

        
        return max(rob_f(root))
        