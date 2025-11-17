# Leetcode Problem 3619 : count islands with total value divisible by K 
# Difficulty : Medium
# Link : https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        columns = len(grid[0])
        row = [0]*(columns + 2)
        for i in range(rows):
            grid[i].insert(0,0)
            grid[i].append(0)
        grid.insert(0,row)
        grid.append(row)
        # for row in grid:
        #     print(row)
        count = 0
        visited = [[0]*(columns+2) for _ in range(rows + 2)]
        queue = []
        for i in range(1,rows+1):
            q_row = []
            index = 0
            for j in range(1,columns+1):
                if( visited[i][j] == 0 and grid[i][j] != 0):
                    # print("I : ", i , " J : ", j)
                    q_row.append((i,j))
                    summ = 0
                    while(q_row):
                        # print("queue start : ", q_row)
                        ele_i, ele_j = q_row.pop()
                        visited[ele_i][ele_j] = 1
                        summ += grid[ele_i][ele_j]
                        
                        if(not visited[ele_i+1][ele_j] and grid[ele_i+1][ele_j] > 0):
                            q_row.append((ele_i+1,ele_j))
                            # summ += grid[ele_i+1][ele_j]
                            visited[ele_i+1][ele_j] = 1

                        if(not visited[ele_i-1][ele_j] and grid[ele_i-1][ele_j] > 0):
                            q_row.append((ele_i-1,ele_j))
                            # summ += gird[ele_i-1][ele_j]
                            visited[ele_i-1][ele_j] = 1

                        if(not visited[ele_i][ele_j-1] and grid[ele_i][ele_j-1] > 0):
                            q_row.append((ele_i,ele_j-1))
                            # summ += grid[ele_i][ele_j-1]
                            visited[ele_i][ele_j-1] = 1

                        if(not visited[ele_i][ele_j+1] and grid[ele_i][ele_j+1] > 0):
                            q_row.append((ele_i, ele_j+1))
                            # summ += grid[ele_i][ele_j+1]
                            visited[ele_i][ele_j+1] = 1
                        # print("Queue : ", q_row)
                    # print("SUMM : ", summ)
                    if(summ %k == 0):
                        count+=1
        return count
    
# Time Complexity : O(m*n) where m is number of rows and n is number of columns
# Space Complexity : O(m*n) for visited array
# Explanation : We use BFS to traverse each island and calculate the sum of its elements.