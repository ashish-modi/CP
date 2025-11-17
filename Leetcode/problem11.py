# Leetcode Problem 11: Container With Most Water
# Difficulty: Medium
# URL: https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        maximum = 0
        left = 0 
        right = length -1
        while(left < right):
            val = min(height[right], height[left])*(right - left)
            maximum = max(maximum, val)
            if(height[right] < height[left]):
                right -=1
            else:
                left +=1
        return maximum
    
# Time complexity:
# O(N) - We use a single pass with two pointers to find the maximum area.
# Space complexity:
# O(1) - We use a constant amount of extra space for the two pointers and maximum variable.
# Explanation:
# The solution uses the two-pointer technique to find the maximum area of water that can be contained. 
# We start with one pointer at the beginning (left) and another at the end (right) of the height array. 
# We calculate the area formed between the two pointers and update the maximum area found so far. 
# Depending on the heights at the two pointers, we move the pointer pointing to the shorter line inward, as this may lead to a larger area. 
# This process continues until the two pointers meet.