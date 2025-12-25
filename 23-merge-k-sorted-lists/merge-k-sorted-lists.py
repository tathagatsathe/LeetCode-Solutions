# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        ans = None
        temp = None
        for i in range(len(lists)):
            if lists[i]!=None:
                heapq.heappush(h, (lists[i].val, i))

        while h:
            num, list_no = heapq.heappop(h)
            if temp == None:
                temp = ListNode(num)
                ans = temp
            else:
                temp.next = ListNode(num)
                temp = temp.next
            if lists[list_no].next!=None:
                lists[list_no] = lists[list_no].next
                heapq.heappush(h, (lists[list_no].val, list_no))

        return ans