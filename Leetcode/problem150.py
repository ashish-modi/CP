# Leetcode Problem 150: Evaluate Reverse Polish Notation
# Difficulty : Medium
# Link : https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        length = len(tokens)
        stack = deque()
        for i in range(length):
            if(tokens[i] == "+"):
                ele2 = stack.pop()
                ele1 = stack.pop()
                stack.append(ele1 + ele2)
            elif(tokens[i] == "-"):
                ele2 = stack.pop()
                ele1 = stack.pop()
                stack.append(ele1 - ele2)
            elif(tokens[i] == "/"):
                ele2 = stack.pop()
                ele1 = stack.pop()
                res = int(ele1 / ele2)
                stack.append(res)
            elif(tokens[i] == "*"):
                ele2 = stack.pop()
                ele1 = stack.pop()
                stack.append(ele1 * ele2)
            else:
                stack.append(int(tokens[i]))
            # print("stack. :", stack)
        return stack.pop()
    
# Time Complexity : O(N)
# Space Complexity : O(N)