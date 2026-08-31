# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def dfs(node):
            if not node:
                return 0
            
            # Recursively find the height of left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # The path through the current node is left_height + right_height
            # Update the global diameter if this path is longer
            self.diameter = max(self.diameter, left_height + right_height)
            
            # Return the height of the current node to its parent
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return self.diameter