# Leetcode Problem 856 : Score of Parentheses
# Difficulty: Medium
# URL: https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        length = len(s)
        depth = 0
        result = 0
        for i in range(length):    
            if(s[i] == "("):
                depth +=1
            else:
                depth -= 1
                if s[i-1] == '(':
                    result += 2 ** depth
        return result
    
# Time complexity: O(N) where N is the length of the input string s.
# Space complexity: O(1) as we are using only a constant amount of extra space to store the depth and result variables.
# Explanation: The solution iterates through the input string s and uses a variable depth to keep track of the current depth of nested parentheses. 
# Whenever it encounters an opening parenthesis '(', it increments the depth. When it encounters a closing parenthesis ')',it decrements the depth. 
# If the closing parenthesis is immediately preceded by an opening parenthesis, it means we have found a complete pair of parentheses, and we add 2 
# raised to the current depth to the result. This is because the score of a pair of parentheses is 1, and if there are nested parentheses, the score is multiplied by 2 for each level of nesting.