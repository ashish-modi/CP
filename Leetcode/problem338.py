# Leetcode Problem 338: Counting Bits
# Difficulty : Easy
# Link : https://leetcode.com/problems/counting-bits/
# Based on Dynamic Programming and Bit Manipulation

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        for i in range(n+1):
            ans[i] = bin(i).count('1')
        return ans

# Time Complexity : O(N) where N is the input number.
# Space Complexity : O(1) as we are using only constant space.