# Problem : Number of Islands (Medium)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if(grid == []):
            return 0
        rows = len(grid)
        cols = len(grid[0])
        zero_row = ["0"]*cols
        grid.insert(0,zero_row)
        grid.append(zero_row)
        for i in range(rows+1):
            grid[i].insert(0,"0")
            grid[i].append("0")

        visited = [[0]*(cols+2) for _ in range(rows+2)]
        count = 0
        for i in range(1,rows+1):
            for j in range(1, cols+1):
                queue = []
                flag = 0
                if(not visited[i][j] and grid[i][j] == "1"):
                    visited[i][j] = 1
                    queue.append((i,j))
                while(queue):
                    ele_i, ele_j = queue.pop(0)
                    if(not visited[ele_i+1][ele_j] and grid[ele_i+1][ele_j] == "1"):
                        visited[ele_i+1][ele_j] = 1
                        queue.append((ele_i+1,ele_j))
                    if(not visited[ele_i-1][ele_j] and grid[ele_i-1][ele_j] == "1"):
                        visited[ele_i-1][ele_j] = 1
                        queue.append((ele_i-1, ele_j))
                    if(not visited[ele_i][ele_j+1] and grid[ele_i][ele_j+1] == "1"):
                        visited[ele_i][ele_j+1] = 1
                        queue.append((ele_i,ele_j+1))
                    if(not visited[ele_i][ele_j-1] and grid[ele_i][ele_j-1] == "1"):
                        visited[ele_i][ele_j-1] = 1
                        queue.append((ele_i,ele_j-1))
                    flag = 1
                if(flag):
                    count +=1
        return count