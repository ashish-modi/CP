# Leetcode Problem 3697: Compute Decimal Representation
# Difficulty : Easy
# Link : https://leetcode.com/problems/compute-decimal-representation/


class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        power = 0
        queue = deque()
        while(n):
            digit = n% 10
            val = digit * (10**power)
            if(val > 0):
                queue.appendleft(val)
            power +=1
            n//=10
        return list(queue)
            
# Time Complexity : O(log N) where N is the input number.
# Space Complexity : O(log N) as we are using extra space for queue.
# Explaination :
# The function decimalRepresentation takes an integer n as input and returns its decimal representation as a list of integers.
# It extracts each digit of the number starting from the least significant digit, calculates its value based on its position, and appends it to a deque.
# Finally, it converts the deque to a list and returns it.