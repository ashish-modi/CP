# Leetcode Problem 994: Rotting Oranges
# Difficulty: Medium
# https://leetcode.com/problems/rotting-oranges/    


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh = levels = 0
        p = deque()
        for i in range(rows):
            for j in range(cols):
                if(grid[i][j] == 1):
                    fresh +=1
                elif(grid[i][j] == 2):
                    p.append((i,j))

        while(fresh and p):
            length = len(p)
            while(length):
                i,j = p.popleft()
                length-=1
                if(i-1 > -1 and grid[i-1][j] == 1):
                    p.append((i-1, j))
                    fresh-=1
                    grid[i-1][j] = 2
                if(i+1 < rows and grid[i+1][j] ==1):
                    p.append((i+1, j))
                    fresh -=1
                    grid[i+1][j] = 2
                if(j-1 > -1 and grid[i][j-1] ==1):
                    p.append((i, j-1))
                    fresh -=1
                    grid[i][j-1] = 2
                if(j+1 < cols and grid[i][j+1] ==1):
                    p.append((i, j+1))
                    fresh -=1    
                    grid[i][j+1] = 2
            levels +=1
        
        return -1 if fresh else levels
    
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)  
# Explanation:
# 1. We first count the number of fresh oranges and add the positions of all rotten oranges to a queue.
# 2. We then perform a breadth-first search (BFS) to rot the adjacent fresh oranges level by level.
# 3. For each level of BFS, we increment the levels counter.
# 4. Finally, if there are still fresh oranges left, we return -1; otherwise, we return the number of levels (minutes) taken to rot all oranges.