# Leetcode Problem 678: Valid Parenthesis String
# Difficulty: Medium
# URL: https://leetcode.com/problems/valid-parenthesis-string/

class Solution:
    def checkValidString(self, s: str) -> bool:
        length = len(s)
        op_stack = deque()
        star_stack = deque()
        for i in range(length):
            if(s[i] == '('):
                op_stack.append(('(',i))
            elif(s[i] == '*'):
                star_stack.append(('*',i))
            else:
                if(op_stack):
                    op_stack.pop()
                elif(star_stack):
                    star_stack.pop()
                else:
                    return False
        
        while(op_stack):
            if(star_stack and op_stack[-1][1] < star_stack[-1][1]):
                op_stack.pop()
                star_stack.pop()
            else:
                return False
        return True
            
            
        
# Time complexity: O(N) where N is the length of the string.
# Space complexity: O(N) for the stacks used to store parentheses and asterisks
# Explanation: The solution uses two stacks to keep track of the positions of open parentheses and asterisks.
# It iterates through the string, pushing open parentheses and asterisks onto their respective stacks.
# When a closing parenthesis is encountered, it tries to match it with an open parenthesis first, and if none are available, it uses an asterisk as a wildcard.
# After processing the entire string, it checks if any unmatched open parentheses can be matched with remaining asterisks based on their positions. 
# If all open parentheses can be matched, the string is valid.