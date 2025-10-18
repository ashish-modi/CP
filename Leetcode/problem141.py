# Leetcode Problem 141: Linked List Cycle
# Difficulty : Easy
# Link : https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointer = head
        while(pointer is not None):
            if(pointer.val is True):
                return True
            pointer.val = True
            pointer = pointer.next
        return False
    
# Time Complexity: O(n)
# Space Complexity: O(1)
# Explanation: We traverse the linked list and mark each visited node by setting its value to True.
# If we encounter a node that is already marked, it indicates a cycle in the list.