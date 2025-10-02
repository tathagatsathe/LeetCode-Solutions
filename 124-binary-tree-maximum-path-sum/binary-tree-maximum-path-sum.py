# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val

        def maxPath(node):
            nonlocal ans

            if node.left==None and node.right==None:
                if node.val > ans:
                    ans = node.val
                return [node.val]

            temp = node.val
            q1 = node.val
            q2 = node.val
            if node.left != None:
                p1 = maxPath(node.left)
                p1_max = max(p1)
                temp+=p1_max
                q1+=p1_max
                # print(node.val, p1)
                # print(node.val, p1, temp, q1, q2)
            if node.right != None:
                p2 = maxPath(node.right)
                p2_max = max(p2)
                temp+=p2_max
                q2+=p2_max
                # print(node.val, p2)

            temp = max(max(temp, max(q1,q2)),node.val)

            if temp > ans:
                ans = temp
            # print('arr: ',[q1, q2, node.val])
            return [q1, q2, node.val]

        maxPath(root)

        return ans

        