# Leetcode Problem: Climbing Stairs 
# Difficulty: Easy
# Link: https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    
# Time Complexity: O(n)
# Space Complexity: O(n)
# Note: This is a dynamic programming solution to find the number of distinct ways to climb to the top of a staircase with n steps.