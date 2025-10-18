# Leetcode Problem 206: Reverse Linked List
# Difficulty : Easy
# Link : https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        if(head):
            next_pointer = head.next
        else:
            return head
        while(next_pointer is not None):
            tmp = pointer
            pointer = next_pointer
            if(tmp == head):
                tmp.next = None
            next_pointer = next_pointer.next
            pointer.next = tmp
        return pointer
    
# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: We use two pointers to reverse the linked list iteratively.