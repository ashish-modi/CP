# Leetcode Problem 155: Min Stack
# Difficulty: Medium
# Link: https://leetcode.com/problems/min-stack/description/

class MinStack:

    def __init__(self):
        self.stack = deque()
        self.minimum = deque()


    def push(self, val: int) -> None:
        if(not self.stack):
            self.min_value = val
        else:
            self.min_value = min(self.minimum[-1],val)
        self.minimum.append(self.min_value)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# Time Complexity: O(1) for all operations
# Space Complexity: O(n) for storing elements in the stack and minimum stack
# Explanation:
# 1. We maintain two stacks: one for the actual stack elements and another for tracking