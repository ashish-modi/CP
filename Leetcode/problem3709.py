# Leetcode Problem 3709: Design Exam Score Tracker
# Difficulty: Medium
# https://leetcode.com/problems/design-exam-score-tracker/description/

class ExamTracker:

    def __init__(self):
        self.start = {}
        self.score = [0]*(100002)
        self.times = [0]*(100002)
        self.dp = [0]*(100002)
        self.index = 1

    def record(self, time: int, score: int) -> None:
        self.start[time] = self.index
        self.times[self.index] = time
        self.score[self.index] = score
        self.dp[self.index] = self.dp[self.index -1] + score
        self.index +=1
        

    def binarySearch(self, left, right, value, starting):
        
        if left > right:
            return -1

        mid = (left + right) // 2

        if starting:
        
            if self.times[mid] >= value:
        
                left_result = self.binarySearch(left, mid - 1, value, starting)
                return mid if left_result == -1 else left_result
            else:
                return self.binarySearch(mid + 1, right, value, starting)
        else:
        
            if self.times[mid] <= value:
        
                right_result = self.binarySearch(mid + 1, right, value, starting)
                return mid if right_result == -1 else right_result
            else:
                return self.binarySearch(left, mid - 1, value, starting)
        
    def totalScore(self, startTime: int, endTime: int) -> int:
        
        start_index = self.binarySearch(0, self.index-1, startTime, True)
        end_index = self.binarySearch(start_index, self.index-1, endTime, False)
    
        if start_index == -1 or end_index == -1 or start_index > end_index:
            return 0
            
        result = self.dp[end_index] - self.dp[start_index] + self.score[start_index]
        return result
        

# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)

# Time Complexity: O(log n) for totalScore, O(1) for record
# Space Complexity: O(n)