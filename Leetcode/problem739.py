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
# Explanation:
# 1. We use a stack to keep track of the temperatures and their indices.
# 2. We iterate through the list of temperatures.
# 3. For each temperature, we check if it is greater than the temperature at the top of the stack.
# 4. If it is, we pop the stack and calculate the number of days until a warmer temperature for the popped index.
# 5. We continue this process until the stack is empty or the current temperature is not greater than the top of the stack.
# 6. Finally, we return the result list containing the number of days until a warmer temperature for each day.