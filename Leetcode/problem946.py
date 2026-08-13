# Leetcode problem 946: Validate Stack Sequences
# Difficulty: Medium
# URL: https://leetcode.com/problems/validate-stack-sequences/

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        dictionary = {}
        pop_index = 0
        push_index = 0
        stack = []
        while True:
            while(pop_index < len(popped) and popped[pop_index] not in dictionary):
                if(push_index < len(pushed)):
                    stack.append(pushed[push_index])
                    dictionary[pushed[push_index]] =1
                    push_index +=1
                else:
                    return False
            if(stack[-1] == popped[pop_index]):
                pop_index +=1
                stack.pop()
            else:
                return False
            if(pop_index == len(popped) and push_index == len(pushed)):
                break
        return True


# Time complexity : O(n) where n is the number of elements in the pushed and popped arrays.
# Space complexity : O(n) where n is the number of elements in the pushed and popped arrays.
# Explanation : The solution uses a stack to simulate the push and pop operations.
# We iterate through the popped array and for each element, we check if it is present in the dictionary (which keeps track of the elements that have been pushed onto the stack). 
# If the element is not present in the dictionary, we keep pushing elements from the pushed array onto the stack until we find the element or we have pushed all elements from the pushed array. 
# If we find the element, we pop it from the stack and move to the next element in the popped array. 
# If we cannot find the element in the stack or if we have pushed all elements from the pushed array and still cannot find the element, we return False. 
# If we successfully iterate through the popped array and the stack is empty at the end, we return True.