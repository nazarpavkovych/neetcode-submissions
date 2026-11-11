# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        visited = [(root,1)]
        depth = 0
        while len(visited)>0:
            node,count = visited.pop()
            if count > depth:
                depth = count
            if node and node.left is not None:
                visited.append((node.left,count+1))
            if node and node.right is not None:
                visited.append((node.right,count+1))
        return depth
            
        
        