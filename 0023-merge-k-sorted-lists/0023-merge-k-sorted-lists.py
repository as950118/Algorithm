# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == []:
            return None
        if len(lists) == 1:
            return lists[0]
        nodes = []
        for l in lists:
            while l:
                nodes.append(l)
                l = l.next
        nodes.sort(key=lambda x:x.val)
        n = len(nodes)
        for i in range(1, n):
            nodes[i-1].next = nodes[i]
        return nodes[0] if nodes else None
