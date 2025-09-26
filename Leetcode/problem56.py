# Leetcode Problem : Merge Intervals
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