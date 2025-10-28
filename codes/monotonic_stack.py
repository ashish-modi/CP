# Monotonic Stack Approach
from collections import deque
from typing import List

def monotonicStackApproach(self, nums: List[int]) -> int:
    length = len(nums)
    right = [-1]*length
    result = 0
    stack = deque()
    for i in range(length):
        while(stack and (nums[i] > nums[stack[-1]])):
            index = stack.pop()
            right[index] = i        
        stack.append(i)

# Explanation: This loop iterates through the array to find the next greater element for each element using a monotonic stack. 
# If the current element is greater than the element at the index stored at the top of the stack, it pops the index from the stack and updates the `right` array with the current index.

# Time Complexity : O(N) where N is the number of elements in the input array.
# Space Complexity : O(N) as we are using extra space for left and right arrays.
   