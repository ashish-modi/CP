# Leetcode Problem 64: Minimum Path Sum
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minSum(self, grid, dp, i, j, curr_sum, rows, cols):
        if(i == rows-1 and j == cols-1):
            dp[i][j] = grid[i][j]
            return curr_sum + grid[i][j]
        if(dp[i][j] != -1):
            return dp[i][j]
        if(i == rows or j == cols):
            return 0
        # move right
        right = down = float('inf')
        if(j < cols-1):
            right = grid[i][j] + self.minSum(grid, dp, i, j+1, curr_sum, rows, cols)
        # move down
        if(i < rows-1):
            down = grid[i][j] + self.minSum(grid, dp, i+1, j, curr_sum, rows, cols)
        
        dp[i][j] = min(right, down)
        return dp[i][j]

    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[-1]*(cols+1) for _ in range(rows + 1)]
        answer =  self.minSum(grid, dp, 0, 0, 0, rows, cols)
        return answer
    
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
# Note: This is a recursive solution with memoization for calculating the minimum path sum in a grid.
# Explanation:
# 1. We define a helper function `minSum` that takes the current position (i, j) and calculates the minimum path sum from that position to the bottom-right corner of the grid.
# 2. We use a 2D list `dp` to store the results of subproblems to avoid redundant calculations (memoization).
# 3. The function explores two possible moves: moving right and moving down, and recursively calculates the minimum path sum for each move.