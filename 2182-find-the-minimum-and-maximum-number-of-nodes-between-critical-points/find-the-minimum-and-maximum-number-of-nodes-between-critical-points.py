# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        next_ = curr.next

        ans = [float("inf"), float("-inf")]
        i = 0
        left_most_idx = right_most_idx = critical_point = None

        while next_:
            if prev.val > curr.val < next_.val or prev.val < curr.val > next_.val:
                if left_most_idx == None:
                    left_most_idx = i
                if critical_point != None:
                    ans[0] = min(i - critical_point, ans[0])
                    ans[1] = i - left_most_idx
                critical_point = i
            i+=1
            prev, curr, next_ = curr, next_, next_.next

        if ans[0] == float("inf"):
            return [-1,-1]
        
        return ans