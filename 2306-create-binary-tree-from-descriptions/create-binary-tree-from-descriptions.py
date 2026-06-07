# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        map_ = {}
        m = {}
        for parent, child, isLeft in descriptions:
            if parent not in m:
                m[parent] = 0
            if child not in m:
                m[child] = 0
            m[child]+=1
            if parent not in map_:
                map_[parent] = ["",""]
            if isLeft:
                map_[parent][0] = child
            else:
                map_[parent][1] = child

        root = None
        for key, count in m.items():
            if count == 0:
                root = key
                break


        root = TreeNode(root)
        dq = deque([root])

        while dq:
            node = dq.popleft()

            if node.val in map_ and map_[node.val][0] != "":
                left_node = TreeNode(map_[node.val][0])
                node.left = left_node
                dq.append(left_node)

            if node.val in map_ and map_[node.val][1] != "":
                right_node = TreeNode(map_[node.val][1])
                node.right = right_node
                dq.append(right_node)


        return root

