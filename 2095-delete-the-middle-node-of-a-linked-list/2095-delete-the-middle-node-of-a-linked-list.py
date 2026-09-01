# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        cur = head
        count = 0
        while cur:
            cur = cur.next
            count += 1

        prv = head
        cur = head
        for i in range(count//2):
            prv = cur
            cur = cur.next
        
        prv.next = cur.next
        return head