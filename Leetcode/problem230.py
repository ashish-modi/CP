# Leetcdode Problem 230: Kth Smallest Element in a BST
# Difficulty: Medium
# Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        elements = deque()
        def helper(root):
            if(root is None):
                return 
            elements.append(root.val)
        
            helper(root.left)
            helper(root.right)
        helper(root)
        
        elements = list(elements)
        heapq.heapify(elements)
        for i in range(k):
            element = heapq.heappop(elements)
        return element
    
# Time Complexity: O(N + k log N) where N is the number of nodes in the BST.
# Space Complexity: O(N) for storing all the elements in the heap.
# Explaination:
# The solution involves performing a traversal of the binary search tree (BST) to collect all the node values into a list. 
# This is done using a helper function that recursively visits each node in the tree and appends its value to a deque.
# After collecting all the values, the list is converted into a min-heap using the heapq library. 
# The k-th smallest element is then found by popping the smallest element from the heap k times. 
# The last element popped from the heap is the k-th smallest element in the BST.
