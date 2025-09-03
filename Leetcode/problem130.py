# Leetcode Problem 130: Surrounded Regions
# Difficulty: Medium
# URL: https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        visited = [[False]*cols for _ in range(rows)]
        result = []
        def dfs(i,j):
            visited[i][j] = True
            if(i-1 > -1 and not visited[i-1][j] and board[i-1][j] == 'O'):    
                up = dfs(i-1,j)

            if(j-1 > -1 and not visited[i][j-1] and board[i][j-1] == 'O'):
                left= dfs(i,j-1)

            if(i+1 < rows and not visited[i+1][j] and board[i+1][j] == 'O'):
                down= dfs(i+1,j)

            if(j+1 < cols and not visited[i][j+1] and board[i][j+1] == 'O'):
                right = dfs(i,j+1)

# Rows and cols are not same
        for i in range(cols):
            if(board[0][i] == 'O'):
                dfs(0,i)

        for i in range(rows):
            if(board[i][0] == 'O'):
                dfs(i,0)

        for i in range(cols): 
            if(board[rows-1][i] == 'O'):
                dfs(rows-1, i)

        for i in range(rows):
            if(board[i][cols-1] == 'O'):
                dfs(i, cols-1)

        for i in range(rows):
            for j in range(cols):
                if(visited[i][j] == False):
                    board[i][j] = 'X'
        
# Time Complexity: O(M*N) where M is number of rows and N is number of columns
# Space Complexity: O(M*N) for visited array in worst case all cells are 'O'