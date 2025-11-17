# Leetcode Problem 42: Trapping Rain Water
# Difficulty: Hard
# URL: https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        stack = deque()
        greater_right = [0]*length
        greater_left = [0]*length
        for i in range(length):
            greater_left[i] = max(height[i], greater_left[i-1]) if i != 0 else height[i]
        while(stack):
            stack.pop()
        for i in range(length-1, -1, -1):
            greater_right[i] = max(height[i], greater_right[i+1]) if i != length -1 else height[i]
        water = 0
        for i in range(length):
            if(greater_left[i] != -1 and greater_right[i] != -1):
                val = min(greater_left[i], greater_right[i]) - height[i]
                water += val
        return water

# Time complexity:
# O(N) - We traverse the height array multiple times, but each traversal is linear in time.
# Space complexity:
# O(N) - We use two additional arrays to store the maximum heights to the left and right of each index.
# Explanation:
# The solution calculates the amount of water that can be trapped at each index by determining the maximum heights to the left and right of that index. 
# We create two arrays, `greater_left` and `greater_right`, to store these maximum heights. 
# For each index, the water that can be trapped is determined by the minimum of the two maximum heights minus the height at that index. 
# We sum up the trapped water for all indices to get the total amount of trapped rain water.

