# Leetcode Problem 226: Invert Binary Tree
# Difficulty: Easy
# URL: https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        new_node = TreeNode()
        if(root is None):
            return
        if(root.left is None and root.right is None):
            new_node.val = root.val
            return new_node
        new_node.val = root.val
        left_node = self.invertTree(root.left)
        right_node = self.invertTree(root.right)
        new_node.left = right_node
        new_node.right = left_node
        return new_node
            
# Time Complexity: O(n)
# Space Complexity: O(h) where h is the height of the tree due to recursion stack
# Explanation: The function recursively inverts the left and right subtrees and swaps them at each node.    