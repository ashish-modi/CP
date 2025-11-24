# Leetcode problem 452: Minimum Number of Arrows to Burst Balloons
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        length = len(points)
        points.sort(key = lambda x: x[1])
        arr_pos = points[0][1]
        arrows = 1
        for i in range(1, length):
            l, r = points[i]
            if(l <= arr_pos <= r):
                continue
            else:
                arrows +=1
                arr_pos = r
        return arrows
    
# Time Complexity: O(n log n)
# Space Complexity: O(1)
# Explanation:
# 1. We sort the points based on their end coordinates.
# 2. We initialize the position of the first arrow to the end coordinate of the first balloon.
# 3. We iterate through the sorted points and check if the current balloon can be burst by the current arrow.
# 4. If it can be burst, we continue to the next balloon. If not, we increment the arrow count and update the position of the arrow to the end coordinate of the current balloon.
# 5. Finally, we return the total number of arrows needed.