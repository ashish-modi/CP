# Leetcode Problem 572: Subtree of Another Tree
# Difficulty: Easy
# URL: https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(root is None):
            return False
        if(subRoot is None):
            return True
        
        def sameTree(r1, r2):
            if(r1 is None and r2 is not None) or (r1 is not None and r2 is None):
                return False
            if(not r1 and not r2):
                return True
            if(r1.val == r2.val):
                left = sameTree(r1.left, r2.left)
                right = sameTree(r1.right, r2.right)
                return left and right
            return False
        if(sameTree(root, subRoot)):
            return True

        left_node = self.isSubtree(root.left, subRoot)
        right_node = self.isSubtree(root.right,subRoot)
        return left_node or right_node
        

# Time Complexity: O(N*M) where N is number of nodes in root and M is number of nodes in subRoot
# Space Complexity: O(H) where H is the height of the tree due to recursion stack
# Explaination: The function checks if subRoot is a subtree of root by comparing each node in root with subRoot using a helper function sameTree. 
# If a match is found, it returns True; otherwise, it continues searching in the left and right subtrees.