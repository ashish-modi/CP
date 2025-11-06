# LeetCode Problem 22: Generate Parentheses
# Difficulty: Medium
# URL: https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def paren(open_count, closed_count):
            if(open_count == closed_count == n):
                res.append("".join(stack))
            if(open_count < n):
                stack.append("(")
                paren(open_count +1, closed_count)
                stack.pop()
            if(closed_count < open_count):
                stack.append(")")
                paren(open_count, closed_count +1)
                stack.pop()
        paren(0,0)
        return res
    
# Time complexity: O(4^n / sqrt(n)) - This is the nth Catalan number, which represents the number of valid parentheses combinations.
# Space complexity: O(4^n / sqrt(n)) - This is the space required to store the result list containing all valid combinations.
# Explanation: The solution uses a backtracking approach to generate all valid combinations of parentheses.
# It maintains a stack to build the current combination and two counters to track the number of open and closed parentheses used.
# The recursive function adds an open parenthesis if there are still open parentheses left to add, and a closed parenthesis if it won't exceed the number of open parentheses.
# When a valid combination is formed (when both counters reach n), it is added to the result list.
