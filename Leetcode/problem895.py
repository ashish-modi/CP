# Leetcode problem 895: Maximum Frequency Stack
# Difficulty: Hard
# URL: https://leetcode.com/problems/maximum-frequency-stack/

import heapq
class FreqStack:

    def __init__(self):
        self.stack = []
        self.counter = 0
        self.dictionary = {}
        

    def push(self, val: int) -> None:
        if(self.dictionary.get(val, 0)):
            self.dictionary[val] +=1
        else:
            self.dictionary[val] = 1
        heapq.heappush(self.stack,[-self.dictionary[val], -self.counter, val])
        self.counter +=1
        
    def pop(self) -> int:
        element_list = heapq.heappop(self.stack)
        
        self.dictionary[element_list[2]] -=1
        return element_list[2]


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

# Time complexity : O(log n) for both push and pop operations, 
# where n is the number of elements in the stack. This is because we are using a heap to maintain the order of elements based on their frequency and insertion time.
# Space complexity : O(n) where n is the number of elements in the stack. 
# This is because we are storing all the elements in the stack and also maintaining a dictionary to keep track of the frequency of each element. 
# In the worst case, if all elements are unique, we will have n elements in the stack and n entries in the dictionary.
# Explanation : The solution uses a max heap (priority queue) to keep track of the elements in the stack based on their frequency and insertion time. 
# The dictionary is used to keep track of the frequency of each element. 
# When an element is pushed onto the stack, we update its frequency in the dictionary and add it to the heap with a negative frequency and negative insertion time (to maintain the order of elements with the same frequency). 
# When an element is popped from the stack, we remove it from the heap and update its frequency in the dictionary. 
# The element with the highest frequency (and most recently added in case of ties) will be popped first.