# Leetcode Problem 143: Reorder List
# Difficulty: Medium
# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        pointer = head
        arr = deque()
        count = 0
        while pointer is not None:
            arr.append(pointer.val)
            pointer = pointer.next
            count+=1
        array = list(arr)
        right = count -1
        left = 0
        n = 0
        pointer = head
        while(left <= right):
            if(n %2 == 0):
                pointer.val = array[left]
                left +=1
            else:
                pointer.val = array[right]
                right -=1
            pointer = pointer.next
            n+=1
        
# Time Complexity: O(n) where n is the number of nodes in the linked list.
# Space Complexity: O(n) for storing the node values in an array.
# Explanation: We first traverse the linked list to store the values in an array. 
# Then, we use two pointers to reorder the values in the required pattern and update the linked list accordingly.   