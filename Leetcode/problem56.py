# Leetcode Problem 56: Merge Intervals
# Difficulty : Medium
# Link : https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        length = len(intervals)
        result = []
        for i in range(1,length):
            if(intervals[i][0] > end):
                result.append([start,end])
                start = intervals[i][0]
                end = intervals[i][1]
            elif(intervals[i][1] > end):
                end = intervals[i][1]
        result.append([start,end])
        return result
    
# Time complexity : O(N)
# Space complexity : O(1)
# Explanation:
# 1. We first sort the intervals based on their starting times.
# 2. We then iterate through the sorted intervals and merge them if they overlap. If they don't overlap, we add the previous interval to the result list and update the start and end to the current interval.
# 3. Finally, we add the last interval to the result list.