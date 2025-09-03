class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            grid[i].insert(0,0)
            grid[i].append(0)
        grid.insert(0,[0]*(cols+2))
        grid.append([0]*(cols + 2))
        for row in grid:
            print(row)
        dp = [[0]*(cols+2) for _ in range(rows+2)]
        for i in range(1,cols+1):
            dp[1][i] = 1 if(grid[1][i] == 0) else 0
        for i in range(1, rows +1):
            dp[i][1] = 1 if(grid[i][1] == 0) else 0
        for i in range(2,rows+1):
            for j in range(2,cols+1):
                if(grid[i][j] == 1):
                    dp[i][j] = 0
                    continue
                diagonal = 0
                if(grid[i-1][j] or grid[i][j-1]):
                    diagonal = dp[i-1][j-1]
                dp[i][j] = diagonal + (dp[i-1][j]) + dp[i][j-1]
                
        
        print("DP ")
        for row in dp:
            print(row)