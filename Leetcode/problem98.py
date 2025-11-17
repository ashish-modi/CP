# Leetcode Problem 98 : Validate Binary Search Tree
# Difficulty : Medium
# Link : https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, low , high):
            if(root is None):
                return True
            if not (low < root.val < high):
                return False
            left = helper(root.left, low, root.val)
            right = helper(root.right, root.val, high)
            return left and right
        return helper(root, float('-inf'), float('inf'))

# Time Complexity: O(N)
# Space Complexity: O(H) where H is the height of the tree due to recursion stack
# Explaination: We use a helper function that takes a node and the valid range (low, high) for that node's value. We recursively check each node to ensure its value is within the valid range, updating the range as we traverse down the tree.from typing import Optional