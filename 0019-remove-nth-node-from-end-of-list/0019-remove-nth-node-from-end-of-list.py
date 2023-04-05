# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        now = head
        for _ in range(n):
            now = now.next
        target = head
        if now == None:
            return target.next
        while now.next != None:
            now = now.next
            target = target.next
        target.next = target.next.next
        return head
            
        