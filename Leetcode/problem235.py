# Leetcode problem 235: Lowest Common Ancestor of a Binary Search Tree
# Difficulty: Medium
# Link : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root, p, q):
            if(root is None):
                return (False , float('inf'))
            left, left_val = helper(root.left, p, q)
            right, right_val = helper(root.right, p, q)
            
            if(left and right) or (root.val == p.val or root.val == q.val):
                return (True, root.val) 
            elif(left):
                return (left, left_val)
            elif(right):
                return (right, right_val)
            else:
                return (False, float('inf'))
        res, val = helper(root, p, q)
        return TreeNode(val)
    
# Time Complexity: O(N) where N is number of nodes in the tree
# Space Complexity: O(H) where H is height of the tree due to recursive stack
# Explanation: We perform a DFS traversal of the tree. For each node, we check if either of its subtrees contains p or q. 
# If both subtrees contain one of the nodes, then the current node is their lowest common ancestor. 
# If only one subtree contains either p or q, we propagate that information up the tree. If neither subtree contains p or q, we return False.