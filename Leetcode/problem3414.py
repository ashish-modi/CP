# Leetcode Problem 3414: Maximum Score of Non-Overlapping Intervals
# Difficulty: Hard
# https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/

class Solution:
    def findmax(self, intervals, dp, length, curr_index, last_inc, res):
        if(curr_index == length):
            return 0, res
        if(dp[last_inc][curr_index][0] != -1):
            return dp[last_inc][curr_index]
        include = 0
        if(last_inc == -1):
            include, inc_res = self.findmax(intervals, dp, length, curr_index + 1, curr_index, res)
            include += (intervals[curr_index][1] - intervals[curr_index][0] +1)* intervals[curr_index][2]
        else:
            if(intervals[last_inc][1] < intervals[curr_index][0] ):
                include, inc_res = self.findmax(intervals, dp, length, curr_index +1, curr_index, res)
                include += (intervals[curr_index][1] - intervals[curr_index][0] +1)* intervals[curr_index][2]
        exclude, exc_res = self.findmax(intervals, dp, length, curr_index+1 , last_inc, res)
        if(include > exclude):
            # print(f"At {curr_index} including with score : {include}, {inc_res}")
            dp[last_inc][curr_index] = (include, inc_res + [curr_index])
        else:
            # print(f"At {curr_index} excluding with score : {exclude}, {exc_res}")
            dp[last_inc][curr_index] = (exclude, exc_res)
        return dp[last_inc][curr_index]

    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        length = len(intervals)
        dp = [[(-1, [])]*length for _ in range(length)]
        dictionary = {}
        for i in range(length):
            dictionary[tuple(intervals[i])] = i+1
        intervals.sort()
        print("INtervals : ", intervals)
        result =  self.findmax(intervals, dp, length, 0, -1, [])[1]
        # for row in dp:
        #     print(row)
        # print("RESULT : ", result)
        # print("Dictionary : ", dictionary )
        res = []
        for val in result:
            res.append(dictionary[tuple(intervals[val])] -1 )
        # print("res: ", res)
        return sorted(res)