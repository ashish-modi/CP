# Problem: Minimum Cost to Cut a Stick
# Difficulty: Hard
# Link: https://leetcode.com/problems/minimum-cost-to-cut-a-stick/description/ 

class Solution:
    def minC(self, left, right, cuts, dp):
        
        if(right - left <= 1):
            dp[left][right] = 0
            return dp[left][right]
   
        if(dp[left][right] != -1):
            return dp[left][right]
       
        cost = float('inf')
        for c in range(left +1, right):
            pick_left = self.minC(left, c , cuts, dp)
            pick_right = self.minC(c, right, cuts, dp)
            pick = (cuts[right] - cuts[left]) + pick_left + pick_right
            cost = min(cost, pick)

        dp[left][right] =  0 if cost == float('inf') else cost
        return dp[left][right]

    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + sorted(cuts) + [n]
        length_cuts = len(cuts)
        dp = [[-1]*(length_cuts + 1) for _ in range(length_cuts +1)]
        return self.minC(0, length_cuts -1, cuts, dp)

# Time Complexity: O(m^3)
# Space Complexity: O(m^2)
# Note: This is a recursive solution with memoization for calculating the minimum cost to cut a stick.    