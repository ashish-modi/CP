# Leetcode Problem 21: Merge Two Sorted Lists
# Difficulty : Easy
# Link : https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        head = None
        pointer1 = list1
        pointer2 = list2
        while (pointer1 is not None) or (pointer2 is not None):
            new_node = ListNode()
            
            if(pointer2 is None) or (pointer1 is not None and pointer1.val <= pointer2.val):
                
                new_node.val = pointer1.val
                pointer1 = pointer1.next
            elif(pointer1 is None) or (pointer2 is not None and pointer1.val > pointer2.val):
            
                new_node.val = pointer2.val
                pointer2 = pointer2.next
            if(res is None):
                res = new_node
                head = res
            else:
                res.next = new_node
                res = new_node
            
        return head
            
# Time Complexity: O(n + m) where n and m are the lengths of list1 and list2
# Space Complexity: O(1) (not counting the output list)
# Explanation: We iterate through both lists, comparing the current nodes and appending the smaller one to the merged list. 