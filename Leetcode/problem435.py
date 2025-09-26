# Leetcode Problem 435: Non-overlapping Intervals
# Difficulty : Medium
# Link : https://leetcode.com/problems/non-overlapping-intervals/
# Based on Greedy Algorithm and Sorting (Intervals)

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        length = len(intervals)
        prev = left_count = 0
        for i in range(1,length):
            if(intervals[i][0] < intervals[prev][1]):
                left_count +=1
            else:
                prev = i
        nxt = length-1
        right_count = 0
        for i in range(length-2, -1, -1):
            if(intervals[i][1] > intervals[nxt][0]):
                right_count +=1
            else:
                nxt = i
        return min(left_count, right_count)
    
# Time Complexity : O(N log N) where N is the number of intervals in the input array.
# Space Complexity : O(1) as we are using only constant space.