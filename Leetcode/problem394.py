# Leetcode Problem 394: Decode String
# Difficulty: Medium
# URL: https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        tmp = ""
        number = ""
        output = ""
        for i in range(len(s)):
            if(s[i] == "]"):
                while(stack[-1] != "["):
                    tmp = stack.pop() + tmp
                stack.pop()
                num = stack.pop()
                stack.append(int(num)* tmp)
                tmp = ""
            elif(s[i] == "["):
                stack.append(int(number))
                number = ""
                stack.append(s[i])
            elif(s[i] != '[' or s[i] != ']'):
                if(ord(s[i]) >= 48 and ord(s[i]) <= 57):
                    number += s[i]
                else:
                    stack.append(s[i])

        while(stack):
            output = stack.pop() + output
        return output


# Time complexity : O(n) where n is the length of the input string s.
# Space complexity : O(n) where n is the length of the input string s.
# Explaination : The solution uses a stack to keep track of the characters and numbers in the input string.
# When a closing bracket is encountered, the solution pops characters from the stack until it finds the corresponding opening bracket. 
# It then pops the number of times to repeat the substring and appends the repeated substring back to the stack. 
# Finally, it constructs the output string by popping all remaining characters from the stack.
