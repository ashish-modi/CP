# Leetcode Problem 124: Binary Tree Maximum Path Sum
# Difficulty: Hard
# URL: https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maximum = float('-inf')
        
        def dfs(node):
            nonlocal maximum
            if(not node):
                return 0
            
            left_val = dfs(node.left)
            right_val = dfs(node.right)
            curr_val = max(left_val, right_val, 0) + node.val
            maximum = max(maximum, node.val+left_val + right_val, curr_val)
            return curr_val

        dfs(root)
        return maximum
    
# Time complexity:
# O(N) - We visit each node exactly once in the DFS traversal.
# Space complexity:
# O(H) - The space complexity is determined by the height of the tree due to the recursion stack. In the worst case (a skewed tree), this can be O(N), while for a balanced tree, it is O(log N).
# Explanation:
# The solution uses a depth-first search (DFS) approach to traverse the binary tree. 
# For each node, it calculates the maximum path sum that can be obtained by including that node and potentially extending to its left and right children. 
# The global maximum path sum is updated whenever a higher sum is found. The function returns the maximum path sum found in the entire tree.