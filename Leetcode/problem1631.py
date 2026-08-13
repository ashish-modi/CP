# Leetcode Problem 1631 : Path with minimum effort
# Difficulty : Medium
# URL : https://leetcode.com/problems/path-with-minimum-effort/

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        graph = {(i,j): [] for i in range(rows) for j in range(cols)}
        
        def construct_graph(index_i, index_j):
            if(index_i > 0):
                diff = abs(heights[index_i-1][index_j] - heights[index_i][index_j])
                graph[(index_i,index_j)].append((diff,(index_i-1, index_j)))
            if(index_i < rows-1):
                diff = abs(heights[index_i +1][index_j] - heights[index_i][index_j])
                graph[(index_i,index_j)].append((diff,(index_i+1, index_j)))
            if(index_j > 0):
                diff = abs(heights[index_i][index_j-1] - heights[index_i][index_j])
                graph[(index_i,index_j)].append((diff,(index_i, index_j-1)))
            if(index_j < cols -1):
                diff = abs(heights[index_i][index_j+1] - heights[index_i][index_j])
                graph[(index_i,index_j)].append((diff,(index_i, index_j+1)))

        for i in range(rows):
            for j in range(cols):
                construct_graph(i,j)
        # print("Graph : ", graph)
        heap = [(0,(0,0))]
        distance = {(i,j):float('inf') for i in range(rows) for j in range(cols)}
        visited = {(i,j):False for i in range(rows) for j in range(cols)}
        distance[(0,0)] = 0
        while(heap):
            element = heapq.heappop(heap)
            weight = element[0]
            node = element[1]
            if(visited[node]):
                continue
            visited[node] = True
            for neigh in graph[node]:
                neigh_weight, neigh_node  = neigh[0], neigh[1]
                new_effort = max(distance[node], neigh_weight)
                if(new_effort < distance[neigh_node]):
                    distance[neigh_node] = new_effort
                    heapq.heappush(heap,(new_effort,neigh_node))
        return distance[(rows-1, cols-1)]

            


# Time complexity : O(mn log(mn)) where m and n are the dimensions of the grid
# Space complexity : O(mn) where m and n are the dimensions of the grid
# Explaination : The algorithm uses Dijkstra's approach to find the path with minimum effort.
# It maintains a priority queue to explore nodes in order of increasing effort and updates the minimum effort required to reach each node.