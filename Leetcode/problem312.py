# Leetcode Problem 312: Burst Balloons
# Difficulty: Hard
# URL: https://leetcode.com/problems/burst-balloons/

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums.insert(0,1)
        nums.append(1)
        
        dp = [[-1]*(n+2) for _ in range(n+2)]
        def dfs(l,r):
            
            if(l == r):
                dp[l][r]= nums[l-1] *nums[l]* nums[l+1]
                return dp[l][r]
            if(dp[l][r] != -1):
                return dp[l][r]
            
            maximum = 0
            for i in range(l, r+1):
                curr_val = nums[l-1]*nums[i]*nums[r+1]
                if(i == l):
                    ans = curr_val + dfs(i+1, r)   
                elif(i == r):
                    ans = curr_val + dfs(l, i-1)   
                else:
                    ans = curr_val + dfs(l,i-1) + dfs(i+1, r)
                maximum = max(maximum, ans)
            dp[l][r] = maximum
            return dp[l][r]
        return dfs(1, n)

# Time complexity: O(N^3) where N is the number of balloons.
# Space complexity: O(N^2) for the dp table used to store intermediate results.
# Explanation: The solution uses a dynamic programming approach with memoization to calculate the maximum coins that can be obtained by bursting balloons in an optimal order.
# It defines a recursive function dfs(l, r) that computes the maximum coins obtainable by bursting all balloons between indices l and r.
# The function iterates through each balloon in the range, considering it as the last balloon to be burst,
# and calculates the coins obtained from bursting it along with the coins from the left and right subproblems.
# The results are stored in a dp table to avoid redundant calculations, leading to an overall time complexity of O(N^3).