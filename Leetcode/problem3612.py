# Leetcode Problem 3612 : process strings with special operations 1
# Difficulty: Medium
# Link: https://leetcode.com/problems/process-string-with-special-operations-i/description/

class Solution:
    def processStr(self, s: str) -> str:
        length = len(s)
        result =[]
        for i in range(length):
            if(s[i] == '*'):
                if(result):
                    result.pop()
            elif(s[i] == '#'):
                result += result
            elif(s[i] == '%'):
                result = result[::-1]
            else:
                result.append(s[i])
        return ("").join(result)
    
# Time complexity: O(n) where n is the length of the string s
# Space complexity: O(n) for the result list in the worst case
# Explanation:
# The function processes the input string s by iterating through each character.
# It uses a list to build the result string, handling special characters '*', '#', and '%'
# according to the specified operations. The final result is obtained by joining the list into a string.