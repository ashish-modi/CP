# Leetcode Problem 2: Add Two Numbers
# Difficulty: Medium
# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = l1
        pointer2 = l2
        carry = 0
        length = 0
        while(pointer1 is not None or pointer2 is not None):
            new_node = ListNode()
            if(pointer1 and pointer2):
                r = pointer1.val + pointer2.val + carry
                pointer1 = pointer1.next
                pointer2 = pointer2.next
            elif(pointer1 is None and pointer2 is not None):
                r = pointer2.val + carry
                pointer2 = pointer2.next
            elif(pointer1 is not None and pointer2 is None):
                r = pointer1.val + carry
                pointer1 = pointer1.next
            carry = 1 if r >= 10 else 0
            r = r % 10
            new_node.val = r
            if(length == 0):
                head = new_node
                p = new_node
                length+=1
            else:
                p.next = new_node
                p = p.next
                length+=1
            
        if(carry):
            new_node = ListNode()
            new_node.val = carry
            
            p.next = new_node
            p = p.next
        
        return head
    
# Time Complexity: O(max(m,n)) where m and n are the lengths of the two linked lists.
# Space Complexity: O(max(m,n)) for the new linked list created to store the result
# Explanation: We traverse both linked lists simultaneously, adding corresponding digits along with any carry from the previous addition. 
# We create new nodes for the result linked list as we compute each digit. 
# If there's a carry left after processing both lists, we add an additional node for it.

