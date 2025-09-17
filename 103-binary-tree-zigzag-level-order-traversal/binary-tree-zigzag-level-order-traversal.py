# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root==None):
            return []

        dq = deque([[root]])
        l_to_r = True
        ans = []
        while(dq):
            # print('l_to_r: ',l_to_r)
            arr = []
            add = []
            que = dq.popleft()
            a = []
            print(que)
            for q in que:
                if q.left:
                    add.append(q.left)
                if q.right:
                    add.append(q.right)
                a.append(q.val)

            if l_to_r == False:
                a = a[::-1]
            ans.append(a)
            l_to_r = l_to_r != True
            if add != []:
                dq.append(add)

        return ans

        