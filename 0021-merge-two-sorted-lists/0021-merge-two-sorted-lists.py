# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None: return list2
        if list2 == None: return list1
        ori = list1
        new = list2
        root = list1
        if ori.val > new.val:
             ori, new = new, ori
             root = list2

        while ori.next:
            if ori.next.val >= new.val:
                temp = new.next
                ori.next, new.next = new, ori.next
                if not temp: break
                new = temp
            else:
                ori = ori.next
        if new:
            ori.next = new

        return root