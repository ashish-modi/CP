# Leetcode Problem 746: Minimum Cost Climbing Stairs
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-cost-climbing-stairs/description/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        length = len(cost)
        for i in range(2,length):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[length-1], cost[length-2])
    
# Time Complexity: O(n)
# Space Complexity: O(1)
# Note: This is a dynamic programming solution to find the minimum cost to reach the top of the stairs, where you can either take one or two steps at a time.
# Explanation:
# 1. We iterate through the cost array starting from the third step.
# 2. For each step, we update its cost to be the sum of its original cost and the minimum cost to reach either of the two previous steps.
# 3. Finally, we return the minimum cost between the last two steps, as they represent the cost to reach the top of the stairs.