# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def rek (node):
            if node is not None:
                if node.left is not None:
                    rek(node.left)
                if node.right is not None:
                    rek(node.right)
                if node.left is not None or node.right is not None:
                    node.left,node.right = node.right,node.left
        rek(root)
        return  root
