# Leetcode Problem 417. Pacific Atlantic Water Flow
# Difficulty: Medium
# Link: https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        visited = [[False]*cols for _ in range(rows)]
        result = []
        def dfs(i,j):
            visited[i][j] = True
            if(i-1 > -1 and not visited[i-1][j] and heights[i-1][j] >= heights[i][j]):    
                up = dfs(i-1,j)

            if(j-1 > -1 and not visited[i][j-1] and heights[i][j-1] >= heights[i][j]):
                left= dfs(i,j-1)

            if(i+1 < rows and not visited[i+1][j] and heights[i+1][j] >= heights[i][j]):
                down= dfs(i+1,j)

            if(j+1 < cols and not visited[i][j+1] and heights[i][j+1] >= heights[i][j]):
                right = dfs(i,j+1)

# Rows and cols are not same
        for i in range(cols):
            dfs(0,i)
        for i in range(rows):
            dfs(i,0)
        pacific = [[-1]*cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                pacific[i][j] = visited[i][j]
                visited[i][j] = False
        
        for i in range(cols):    
            dfs(rows-1, i)
        for i in range(rows):
            dfs(i, cols-1)

        for i in range(rows):
            for j in range(cols):
                if(pacific[i][j] and visited[i][j]):
                    result.append([i,j])

        return result

# Time Complexity: O(m*n)
# Space Complexity: O(m*n) 
# Explanation:
# 1. We perform two separate DFS traversals: one for the Pacific Ocean and one for the Atlantic Ocean.
# 2. We start the DFS from the cells adjacent to each ocean and mark the reachable cells in a visited matrix.
# 3. After both DFS traversals, we check which cells are reachable from both oceans by checking the visited matrices.
# 4. We collect the coordinates of these cells and return them as the result.