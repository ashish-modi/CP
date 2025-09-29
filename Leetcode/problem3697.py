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