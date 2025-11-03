# Leetcode Problem 2544: Alternating Digit Sum
# Difficulty: Easy
# URL: https://leetcode.com/problems/alternating-digit-sum/

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        string = str(n)
        length = len(string)
        total = 0
        for i in range(length):
            sign = 1 if(i%2 == 0) else -1
            total += int(string[i])*sign
        return total
    
# Time complexity: O(D) where D is the number of digits in n.
# Space complexity: O(1) as we are using a constant amount of space.
# Explanation: The solution converts the integer n to a string to easily access each digit.