# Leetcode Problem 189 : Rotate Array
# Difficult : Medium
# URL : https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        visited = [0]*length
        curr_index = 0
        start = 0
        while(start < length):
            if(visited[start]):
                start +=1
            if(start >= length):
                break
            curr_ele = nums[start]
            curr_index = start
            while(True):
                next_index = (curr_index + k)% length
                if(visited[next_index] == 0):
                    visited[next_index] = 1
                    tmp = nums[next_index]
                    nums[next_index] = curr_ele
                    curr_index = next_index
                    curr_ele = tmp
                    
                else:
                    start +=1
                    break

# Time complexity : O(n)
# Space complexity : O(n)
# Explanation :
# The algorithm rotates the array in place by moving elements to their new positions in cycles. 
# It uses a visited array to keep track of which elements have been moved to avoid overwriting elements that have not yet been moved. 
# The outer while loop iterates through the array, and the inner while loop performs the rotation for each cycle until all elements have been moved to their correct positions.