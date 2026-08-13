# Problem 901. Online Stock Span
# Difficulty: Medium
# Link : https://leetcode.com/problems/online-stock-span/

class StockSpanner:

    def __init__(self):
        "[(e1, e2)] : e1 -> element, e2 : count"
        self.stack = deque()

    def next(self, price: int) -> int:
        curr = 1
        while(self.stack and price >= self.stack[-1][0]):
            element, count = self.stack.pop()
            curr += count
        self.stack.append((price, curr))
        return curr
        
            

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# Time complexity : O(n)
# Space complexity : O(n) where n is the number of elements in the stack
# Explaination:
# The idea is to use a stack to keep track of the prices and their corresponding spans.
# When a new price is added, we pop elements from the stack until we find a price greater than the current price. 
# For each popped element, we add its count to the current span.