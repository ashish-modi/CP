# Leetcode Problem 1020 : Number of Enclaves
# Difficulty : Medium
# URL : https://leetcode.com/problems/number-of-enclaves/

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0]* cols for i in range(rows)]

        def traverse(i,j):
            visited[i][j] = 1
            if(i > 0 and grid[i-1][j] and not visited[i-1][j]):
                traverse(i-1,j)
            if(i < rows-1 and grid[i+1][j] and not visited[i+1][j]):
                traverse(i+1,j)
            if(j > 0 and grid[i][j-1] and not visited[i][j-1]):
                traverse(i, j-1)
            if(j < cols-1 and grid[i][j+1] and not visited[i][j+1]):
                traverse(i, j+1)


        for i in range(cols):
            if(grid[0][i] and not visited[0][i]): # row 1
                traverse(0,i)
            if(grid[rows-1][i] and not visited[rows-1][i]): # last row
                traverse(rows-1, i)
        for i in range(rows):
            if(grid[i][0] and not visited[i][0]): # col1 
                traverse(i,0)
            if(grid[i][cols-1] and not visited[i][cols-1]): # last col
                traverse(i,cols-1)

        count = 0
        for i in range(rows):
            for j in range(cols):
                if(grid[i][j] and not visited[i][j]):
                    count +=1

        return count

# Time complexity : O(m*n) where m is the number of rows and n is the number of columns in the grid.
# Space complexity : O(m*n) where m is the number of rows and n is the number of columns in the grid.
# Explanation : The solution uses depth-first search (DFS) to traverse the grid and mark visited land cells. 
# The first pass marks all land cells connected to the borders as visited. The second pass counts the remaining unvisited land cells, which are enclaves.