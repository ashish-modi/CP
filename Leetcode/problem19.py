# Leetcode Problem 19: Remove Nth Node From End of List
# Difficulty: Medium
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer1 = head
        pointer2 = None
        count = 0
        while(pointer1 is not None):
            pointer1 = pointer1.next
            count+=1
        traverse = count -n 
        for i in range(traverse):
            if(i == 0):
                pointer2 = head
            else:
                pointer2 = pointer2.next
        
        
        if(pointer2 is None):
            return head.next
        else:
            pointer2.next = pointer2.next.next
            return head
        
# Time Complexity: O(L) where L is the length of the linked list
# Space Complexity: O(1)
# Explanation:
# The solution uses two pointers to find the nth node from the end of the linked list.
# First, it calculates the total length of the linked list.
# Then, it traverses the list again to reach the node just before the target node and
# adjusts the pointers to remove the target node. If the target node is the head,
# it simply returns the next node as the new head.  