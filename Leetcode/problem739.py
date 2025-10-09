# Leetcode Problem 739: Daily Temperatures
# Difficulty: Medium
# URL: https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        stack = deque()
        result = [0]*length
        stack.append([temperatures[0],0])
        # print("stack : ", stack)
        for i in range(1,length):
            while(stack and temperatures[i] > stack[-1][0]):
                result[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append([temperatures[i],i])
            # print("stack : ", stack)
        # print("result : ", result)
        return result
            
# Time complexity : O(n)    
# Space complexity : O(n)