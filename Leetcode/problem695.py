# Leetcode Problem 695: Max Area of Island
# Difficulty: Medium
# Link: https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maximum = 0
        visited = [[0]*(cols) for _ in range(rows)]
        def dfs(i,j):
            visited[i][j] =1 

            right = down = left = up = 0
            if(i+1 < rows and j < cols and (not visited[i+1][j]) and grid[i+1][j]):
                down = dfs(i+1, j)
            if(j+1 < cols and i < rows and (not visited[i][j+1]) and grid[i][j+1]):
                right =  dfs(i, j+1)
            if(i-1 > -1 and j < cols and (not visited[i-1][j]) and grid[i-1][j]):
                up = dfs(i-1, j)
            if(j-1 > -1 and i < rows and (not visited[i][j-1]) and grid[i][j-1]):
                left = dfs(i,j-1)
            
            return visited[i][j] + right + down + left + up
        for i in range(rows):
            for j in range(cols):
                if(not visited[i][j] and grid[i][j]):
                    ans = dfs(i,j)
                    maximum = max(ans, maximum)
        return maximum
    
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
# Note: This is a recursive solution with depth-first search (DFS) to find the maximum area of an island in a grid.
# The solution uses a `visited` array to keep track of the cells that have already been explored to avoid counting them multiple times.
# The `dfs` function explores all four possible directions (up, down, left, right) from the current cell and recursively counts the area of the island.
# The base case checks if the next cell is within bounds, not visited, and is part of the island (value 1).
# The overall maximum area is updated during the iteration over all cells, and the final result is returned.