# Leetcode Problem 84: Largest Rectangle in Histogram
# Difficulty : Hard
# Link : https://leetcode.com/problems/largest-rectangle-in-histogram/
# Based on Stack


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        left = [0]*length
        right = [0]*length
        maximum = 0
        stack = deque()
        stack.append([heights[0],0])
        for i in range(1,length):
            while(stack and heights[i] < stack[-1][0]):
                right[stack[-1][1]] = i
                stack.pop()
            stack.append([heights[i],i])
        while(stack):
            right[stack[-1][1]] = length
            stack.pop()
        # print("right : ", left)
        stack.append([heights[-1],length-1])
        for i in range(length-2, -1, -1):
            while(stack and heights[i] < stack[-1][0]):
                left[stack[-1][1]] = i
                stack.pop()
            stack.append([heights[i],i])
        while(stack):
            left[stack[-1][1]] = -1
            stack.pop()
        # print("left: ", right)
        for i in range(length):
            val = heights[i]*((right[i]-left[i]) -1)
            maximum = max(maximum, val)
        return maximum
    
# Time complexity : O(N) where N is the number of bars in the histogram.
# Space complexity : O(N) as we are using extra space for left and right arrays.
# Explanation : To find the largest rectangle in histogram, we can use a stack-based approach to efficiently calculate the maximum area.
# We maintain two arrays, left and right, to store the indices of the nearest smaller bars to the left and right of each bar. 
# The width of the rectangle for each bar can be calculated using these indices, and the area can be computed as height * width. 
# Finally, we return the maximum area found.
# This approach ensures that we only traverse the heights array a few times, leading to an overall