# Leetcode Problem 3703: Remove K- Balanced Substrings
# Difficulty: Medium
# Link: https://leetcode.com/problems/remove-k-balanced-substrings


class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        length = len(s)
        stack = deque()
        result = deque()
        stack.append([s[0],1])
        for i in range(1,length):
            
            if(s[i] == '('):
                if(stack and stack[-1][0] == s[i]):
                    stack[-1][1] +=1
                else:
                    stack.append([s[i], 1])
            elif(s[i] == ')'):
                if(stack and stack[-1][0] == s[i]):
                    stack[-1][1] +=1   
                else:
                    stack.append([s[i],1])
                if(len(stack) >= 2 and stack[-1][1] >=k):
                    if (stack[-2][0] != s[i]) and (stack[-2][1] >= k):
                        stack[-2][1] -= k
                        stack[-1][1] -=k
                        if(stack[-1][1] == 0):
                            stack.pop()
                        if(stack[-1][1] == 0):
                            stack.pop()
                
        
        while(stack):
            element, count = stack.popleft()
            for i in range(count):
                result.append(element)
        

        return ("").join(list(result))
    
# Time Complexity: O(n)
# Space Complexity: O(n)    
# Explanation: We use a stack to keep track of the characters and their counts. 
# When we encounter a closing parenthesis, we check if we can form a k-balanced substring with the top two elements of the stack. 
# If we can, we reduce their counts by k. Finally, we reconstruct the string from the stack.  