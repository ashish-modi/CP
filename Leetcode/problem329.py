# Leetcode Problem: Longest Increasing Path in a Matrix 
# Difficulty: Hard
# Link: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[-1]*(cols + 1) for _ in range(rows + 1)]
        def dfs(row, col):
            if(dp[row][col] != -1):
                return dp[row][col]

            left = right = up = down = 0
            if(row +1 < rows and matrix[row+1][col] > matrix[row][col]):
                down = 1 + dfs(row+1, col)
            if(row -1 > -1 and matrix[row-1][col] > matrix[row][col]):
                up = 1 + dfs(row -1, col)
            if(col -1 > -1 and matrix[row][col -1] > matrix[row][col]):
                left = 1 + dfs(row, col -1)
            if(col +1 < cols and matrix[row][col+1] > matrix[row][col]):
                right = 1 + dfs(row, col+1)
            dp[row][col] = max(left, right, up, down)
            return dp[row][col]
            
            
        maximum = 0
        for i in range(rows):
            for j in range(cols):
                maximum = max(maximum, dfs(i,j))
        return maximum + 1

# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
# Note: This is a recursive solution with memoization to find the longest increasing path in a matrix.
# The solution uses depth-first search (DFS) to explore all possible paths starting from each cell in the matrix.
# The `dp` array is used to store the length of the longest increasing path starting from each cell, avoiding redundant calculations.
# The function `dfs` checks the four possible directions (up, down, left, right) and recursively explores valid paths where the next cell has a greater value than the current cell.
# The base case checks if the value for the current cell has already been computed, returning it if so.
# The overall maximum path length is updated during the iteration over all cells, and the final result is returned after adding 1 to account for the starting cell itself.