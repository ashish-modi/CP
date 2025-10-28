# Leetcode Problem 778: Swim in Rising Water
# Difficulty: Hard
# URL: https://leetcode.com/problems/swim-in-rising-water/

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        distance = [[float('inf')]*cols for _ in range(rows)]
        graph = {}
        heap = [(0,(0,0))]
        visited = [[0]*cols for _ in range(rows)]
        heapq.heapify(heap)
        for i in range(rows):
            for j in range(cols):
                if(i+1 < rows):
                    graph[(i,j)] = graph.get((i,j),[]) +[(grid[i+1][j],(i+1,j))]
                if(i-1 >= 0):
                    graph[(i,j)] = graph.get((i,j),[]) +[(grid[i-1][j],(i-1,j))]
                if(j+1 < cols):
                    graph[(i,j)] = graph.get((i,j),[]) +[(grid[i][j+1],(i,j+1))]
                if(j-1 >= 0):
                    graph[(i,j)] = graph.get((i,j),[]) +[(grid[i][j-1],(i,j-1))]
        maximum = 0
        while(heap):
            val, indexes = heapq.heappop(heap)
            i,j = indexes
            visited[i][j] = 1
            maximum = max(maximum, grid[i][j])
            if(i == rows - 1 and j == cols-1):
                break
            for neigh in graph[(i,j)]:
                d, i_j = neigh
                index_i, index_j = i_j
                if(not visited[index_i][index_j]):
                    heapq.heappush(heap, neigh)
        return maximum


# Time complexity: O(N log N) where N is the number of cells in the grid.
# Space complexity: O(N) for the distance and visited arrays, and the graph representation.
# Explaination: The solution uses a priority queue (min-heap) to explore the grid in a manner similar to Dijkstra's algorithm. 
# It starts from the top-left corner and explores neighboring cells, always choosing the cell with the lowest elevation that hasn't been visited yet. 
# The maximum elevation encountered along the path to the bottom-right corner is tracked, and this value is returned as the result.
