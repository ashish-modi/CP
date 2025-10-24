# Leetcode Problem 1448: Count Good Nodes in Binary Tree
# Difficulty: Medium
# Link : https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def helper(root, maximum):
            nonlocal count
            if(root is None):
                return 
            
            if(root.val >= maximum):
            
                count+=1
            maximum = max(maximum, root.val)
            helper(root.left, maximum)
            helper(root.right, maximum)
    
        helper(root, float('-inf'))
        
        return count
    
# Time Complexity: O(N) where N is the number of nodes in the binary tree.
# Space Complexity: O(H) where H is the height of the binary tree due to the recursion stack.
# Explanation: The function traverses the binary tree using DFS, keeping track of the maximum value encountered along the path from the root to the current node. 
# If the current node's value is greater than or equal to this maximum, it is counted as a "good" node.