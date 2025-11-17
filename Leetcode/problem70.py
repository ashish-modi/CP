# Leetcode Problem 70: Climbing Stairs 
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
# Explanation:
# 1. We create a list `dp` where `dp[i]` represents the number of ways to reach the i-th step.
# 2. The base cases are `dp[0] = 1` (1 way to stay at the ground) and `dp[1] = 1` (1 way to reach the first step).
# 3. For each step from 2 to n, the number of ways to reach that step is the sum of the ways to reach the two preceding steps (`dp[i-1]` and `dp[i-2]`), since we can reach the i-th step by taking a single step from (i-1) or a double step from (i-2).
# 4. Finally, we return `dp[n]`, which contains the total number of distinct ways to reach the n-th step.