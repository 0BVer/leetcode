# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode(val = 999, next = head)
        p = start
        n = start.next
        now = 999

        while n and n.next:
            now = n.val
            post = n.next.val
            if now == post:
                while now == post:
                    n = n.next
                    if not n.next:
                        break
                    post = n.next.val
                p.next = n.next

            else:
                p.next = n
                p = p.next

            n = p.next
            
        return start.next