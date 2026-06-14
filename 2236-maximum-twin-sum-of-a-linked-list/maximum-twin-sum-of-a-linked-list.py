# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        node = head
        l = []
        while node:
            l.append(node.val)
            node = node.next
            
        n = len(l)
        return max([x+y for x, y in zip(l[:n//2], l[n//2:][::-1])])


        