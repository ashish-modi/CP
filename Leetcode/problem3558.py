# Leetcode problem 3558: Assign Edge Weights to Make Path Length Even
# Difficulty: Medium
# https://leetcode.com/problems/assign-edge-weights-to-make-path-length-even/

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        length = len(edges)
        queue = deque()
        queue.append(1)
        level_elements = 1
        visited = [0]*(length+2)
        visited[1] = 1
        mod_val = 10**9+7
        graph = {}
        levels = new_elements = total = 0
        for edge in edges:
            if(graph.get(edge[0],0)):
                graph[edge[0]].append(edge[1])
            else:
                graph[edge[0]] = [edge[1]]
            if(graph.get(edge[1],0)):
                graph[edge[1]].append(edge[0])
            else:
                graph[edge[1]] = [edge[0]]
        
        while(queue):
            element = queue.popleft()
        
            level_elements -=1
            for neigh in graph[element]:
                
                if(not visited[neigh]):
                    visited[neigh] = 1
                    queue.append(neigh)
                    new_elements +=1
            if(level_elements== 0):
                levels +=1
                level_elements = new_elements
                new_elements = 0
        levels -=1
        return (2**(levels-1))% mod_val
        
            

# Time complexity: O(n) where n is the number of edges
# Space complexity: O(n) for the graph and queue
# Explanation:
# The function assigns edge weights to make the path length even by performing a BFS traversal
# of the graph. It counts the number of levels in the BFS tree and calculates the result
# as 2 raised to the power of (levels - 1), modulo 10^9 + 7. The BFS ensures that all nodes are visited level by level.