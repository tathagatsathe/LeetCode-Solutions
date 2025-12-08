# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        arr = list(range(1, n+1))

        def fn(arr):
            if len(arr) == 0:
                return [None]
            if len(arr) == 1:
                return [TreeNode(arr[0])]

            ans = []
            for i in range(len(arr)):
                l_combinations = fn(arr[:i])
                r_combinations = fn(arr[i+1:])
                for l in l_combinations:
                    for r in r_combinations:
                        node = TreeNode(arr[i])
                        node.left = l
                        node.right = r
                        ans.append(node)

            return ans

        ans = fn(arr)
        return ans
