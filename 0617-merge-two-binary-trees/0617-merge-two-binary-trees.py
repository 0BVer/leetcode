# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if root1 == None and root2 == None: return None
        if root1 == None: root1 = TreeNode()
        if root2 == None: root2 = TreeNode()

        def dfs(n1: TreeNode, n2: TreeNode):
            n1.val += n2.val

            if n1.left != None and n2.left != None:
                dfs(n1.left, n2.left)
            elif n1.left == None and n2.left != None:
                n1.left = TreeNode()
                dfs(n1.left, n2.left)
            
            if n1.right != None and n2.right != None:
                dfs(n1.right, n2.right)
            elif n1.right == None and n2.right != None:
                n1.right = TreeNode()
                dfs(n1.right, n2.right)

        dfs(root1, root2)

        return root1
            

            