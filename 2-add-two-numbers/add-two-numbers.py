# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0

        head = ListNode(1)
        currNode = head

        while l1!=None and l2!=None:
            sum_ = l1.val + l2.val + carry
            carry = 1 if sum_ >=10 else 0
            last_digit = sum_% 10
            currNode.next = ListNode(last_digit)
            currNode = currNode.next
            l1 = l1.next
            l2 = l2.next

        remainingList = None

        if l1!=None:
            remainingList = l1
        elif l2!=None:
            remainingList = l2

        while remainingList!=None:
            sum_ = remainingList.val + carry
            carry = 1 if sum_ >=10 else 0
            last_digit = sum_% 10
            currNode.next = ListNode(last_digit)
            currNode = currNode.next
            remainingList = remainingList.next

        if carry!=0:
            currNode.next = ListNode(carry)

        return head.next

        



