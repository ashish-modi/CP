# Leetcode Problem 1547: Minimum Cost to Cut a Stick
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
# Explanation:
# 1. The function minC computes the minimum cost to cut the stick between indices left and right in the cuts array.
# 2. If there are no cuts to be made (i.e., right - left <= 1), the cost is 0.
# 3. If the result for the current left and right indices is already computed (i.e., dp[left][right] != -1), it returns the stored result.
# 4. It iterates through all possible cuts between left and right, recursively calculating the cost of making each cut and updating the minimum cost.
# 5. The minCost function initializes the cuts array by adding the two ends of the stick (0 and n) and sorts the cuts.
# 6. It initializes a dp table for memoization and calls the minC function to get the final result.