# Leetcode Problem 57: Insert Interval
# Difficulty : Medium
# Link : https://leetcode.com/problems/insert-interval/
# Based on Array and Sorting (Intervals)

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        length = len(intervals)
        i = 0
        result = []
        if(not intervals):
            return [newInterval]
        while(i < length):
            # new interval
            if (i < length-1 and intervals[i][1] < newInterval[0] and intervals[i+1][0] > newInterval[1]) or (i == length-1 and intervals[i][1] < newInterval[0]):
                result.append(intervals[i])
                result.append(newInterval)
                i+=1
            elif (i == 0 and intervals[i][0] > newInterval[1]):
                result.append(newInterval)
                result.append(intervals[i])
                i+=1

            # merge

            elif(intervals[i][0] <= newInterval[0] and intervals[i][1] >= newInterval[0]) or (i == 0 and intervals[i][0] > newInterval[0]) or (i < length-1 and intervals[i][1] < newInterval[0] and intervals[i+1][0] > newInterval[0]):  # starting point
                index = i
                if(intervals[i][0] > newInterval[0]):
                    start = newInterval[0]
                elif (intervals[i][1] < newInterval[0] and intervals[i+1][0] > newInterval[0]):
                    start = newInterval[0]
                    result.append(intervals[i])
                else:
                    start = intervals[i][0]
                while (index < length):
                    if(intervals[index][0] <= newInterval[1] and intervals[index][1] >= newInterval[1]):
                        end = intervals[index][1] 
                        result.append([start,end])
                        i = index + 1
                        break
                    if(newInterval[1] > intervals[index][1]):
                        if(index < length -1 and intervals[index+1][0] > newInterval[1]) or (index == length-1):
                                end = newInterval[1]
                                result.append([start,end])
                                i = index + 1
                                break
                    index+=1
            else:
                result.append(intervals[i])
                i+=1

        return result
    
# Time Complexity : O(N) where N is the number of intervals in the input array.
# Space Complexity : O(N) as we are using extra space for the result array. 
# Explanation:
# 1. We iterate through the list of intervals and determine where to insert the new interval.
# 2. We handle three cases: inserting the new interval before the current interval, merging overlapping intervals, and simply adding the current interval to the result.
# 3. We use a while loop to merge overlapping intervals and update the result list accordingly.