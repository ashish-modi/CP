# Leetcode Problem 191: Number of 1 Bits
# Difficulty : Easy
# Link : https://leetcode.com/problems/number-of-1-bits/
# Based on Bit Manipulation

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while(n>0):
            if(n%2 == 1):
                count +=1
            n//=2
        return count
            
# Time Complexity : O(log N) where N is the input number.
# Space Complexity : O(1) as we are using only constant space.  
# Explanation:
# 1. We initialize a count variable to keep track of the number of 1 bits.
# 2. We use a while loop to iterate through the bits of the input number until n becomes 0.
# 3. In each iteration, we check if the least significant bit is 1 by checking if n % 2 equals 1.
# 4. If it is 1, we increment the count.
# 5. We then right shift the number by dividing it by 2 (using integer division).
# 6. Finally, we return the count of 1 bits.