# Leetcode Problem 3693: Climbing Stairs II
# Difficulty : Medium
# Link : https://leetcode.com/problems/climbing-stairs-ii/

class Solution:
    def climbStairs(self, n: int, cost: List[int]) -> int:
        length = len(cost)
        dp = [0]*length
        dp[0] = cost[0] + 1
        if(length > 1):
            dp[1] = min(cost[1] + 2*2, dp[0] + cost[1] + 1)
        if(length > 2):
            dp[2] =min(cost[2] + 3*3, dp[0] + cost[2] + 2*2, dp[1] + cost[2] + 1)
        for i in range(3,length):
            if(i - 3 > -1):
                dp[i] = min(dp[i-3] + cost[i] + 3*3, dp[i-2] + cost[i] + 2*2, dp[i-1] + cost[i] + 1)
        # print("DP : ", dp)
        return dp[length-1]
    
# Time Complexity : O(N) where N is the number of elements in the input array.
# Space Complexity : O(N) where N is the number of elements in the input array as we are using a dp array of size N.