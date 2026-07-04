# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if k == 1:
            return head
        
        root = ListNode(0)
        root.next = head
        head = root
        pre = root
        root = root.next


        while root:
            node = root

            for i in range(k):
                if node == None:
                    return head.next
                node = node.next

            first_node = root
            kth_node = root
            
            for i in range(k - 1):
                temp = kth_node.next
                kth_node.next = kth_node.next.next
                temp.next = first_node
                first_node = temp

            pre.next = first_node
            pre = kth_node
            root = root.next
                    
        return head.next
