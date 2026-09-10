# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0

        def fn(root):
            nonlocal ans

            if root == None:
                return 0, 0

            left_sum, left_count = fn(root.left)
            right_sum, right_count = fn(root.right)

            total_sum = root.val + left_sum + right_sum
            total_count = 1 + left_count + right_count

            avg = int(total_sum/total_count)

            if avg == root.val:
                ans+=1

            return total_sum,  total_count

        fn(root)

        return ans