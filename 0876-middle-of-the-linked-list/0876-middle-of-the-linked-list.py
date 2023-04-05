# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None: return head
        now, double = head, head.next

        while True:
            now = now.next
            if double.next == None: return now
            double = double.next
            if double.next == None: return now
            double = double.next