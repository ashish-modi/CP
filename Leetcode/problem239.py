# Leetcode Problem 239 : Sliding Window Maximum
# Difficulty : Hard
# Link : https://leetcode.com/problems/sliding-window-maximum/


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        res = [0]*(length-k+1)
        heap = []
        heapq.heapify(heap)
        for left in range(length):
            heapq.heappush(heap, [-nums[left], left])
            if(left >= k-1):
                element, index = -heap[0][0], heap[0][1]
                res[left-k+1] = element
                while(index <= left-k+1):
                    heapq.heappop(heap)
                    if(heap):
                        element, index = -heap[0][0], heap[0][1]
                    else:
                        break
        return res
    
# Time Complexity: O(N log K)
# Space Complexity: O(K)
# Explanation: We use a max-heap to keep track of the maximum element in the current window of size k. 
# As we slide the window from left to right, we add the new element to the heap and remove elements that are out of the current window. 
# The maximum element in the heap is the maximum for the current window. 
# We repeat this process until we have processed all elements in the array.