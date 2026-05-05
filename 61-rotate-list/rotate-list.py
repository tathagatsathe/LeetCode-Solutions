# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        node = head
        while node:
            node = node.next
            n+=1
        
        if n == 0: return head
        
        k = k%n
        if k == 0:
            return head

        node = head
        count = 0
        while count < n - k - 1:
            node = node.next
            count+=1

        temp = node.next
        node.next = None

        node = temp

        while node and node.next != None:
            node = node.next

        if node != None:
            node.next = head

        head = temp

        return head

        
        