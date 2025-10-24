# Leetcode problem 199: Binary Tree Right Side View
# Difficulty: Medium
# URL: https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = [float('inf')]*105
        res = deque()
        def helper(root, level):
            if(root is None):
                return 
            if(levels[level] == float('inf')):
                levels[level] = root.val
                res.append(root.val)
            helper(root.right, level+1)
            helper(root.left, level+1)
        helper(root, 0)
        return list(res)
    
# Time Complexity: O(N)
# Space Complexity: O(H) where H is the height of the tree
# Explanation: We perform a DFS traversal prioritizing the right child first. 
# We keep track of the levels we have seen and add the first node we encounter at each level to the result list.
