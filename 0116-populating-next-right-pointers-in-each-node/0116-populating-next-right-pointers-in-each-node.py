"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution: #tree
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None: return None
        
        head = root
        while head.left:
            head.left.next = head.right
            now = head
            while now.next:
                now.right.next = now.next.left
                now = now.next
                now.left.next = now.right

            head = head.left
        return root
    
# from collections import deque

# class Solution: #bfs
#     def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
#         if root == None: return None
#         root.next = '#'
#         d = deque()
#         d.append(root)
#         while len(d):
#             l = len(d)
#             for i in range(l - 1):
#                 n = d.popleft()
#                 n.next = d[0]
#                 if n.right != None: 
#                     d.append(n.left)
#                     d.append(n.right)
            
#             n = d.popleft()
#             n.next = None
#             if n.right != None: 
#                 d.append(n.left)
#                 d.append(n.right)
        
#         return root