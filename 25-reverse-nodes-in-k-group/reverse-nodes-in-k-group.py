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
        # print(root)
        while root:
            node = root
            
            for i in range(k-1):
                if node!=None:
                    node = node.next

            if node == None:
                break

            p = root
            r = root
            # print('p: ', p)
            
            for i in range(k - 1):
                temp = r.next
                r.next = r.next.next
                temp.next = p
                p = temp

            temp1 = pre
            temp1.next = p
            pre = r
            # print(pre)
            # print('____________________')
            # print(root)
            root = root.next
                    
        return head.next

        



#   r
#   p   nd
# # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9

# temp = r.next.next
# r.next.next = p
# p = r.next
# r.next = temp

# temp = 3
# r.next.next = 1
# r.next = 3

# # 1 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9

#   p    r   
# # 2 -> 1 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9

# temp = 4
# r.next.next = 2   3 -> 2
# p = r.next
# r.next = 4

#   p         r   
# # 3 -> 2 -> 1 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9

# # 1 -> 2 -> 4 -> 3 -> 5 -> 6 -> 7 -> 8 -> 9


