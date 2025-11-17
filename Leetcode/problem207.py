# Porblem 207: Course Schedule
# Difficulty: Medium
# https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        length = len(prerequisites)
        visited = [False]*numCourses
        for edge in prerequisites:
            graph[edge[0]].append(edge[1])
       
        
        done = [False]*numCourses
        def dfs(start):
            visited[start] = True
            if(done[start]):
                return done[start]
            done[start] = True
            for neigh in graph[start]:
                if(not visited[neigh]):
                    if(dfs(neigh)):
                        visited[neigh] = False
                    else:
                        return False
                else:
                    return False
                    
            return True

        for i in range(length):
            if(not done[prerequisites[i][0]]):
                if(not dfs(prerequisites[i][0])):
                    return False
                else:
                    visited[prerequisites[i][0]] = False
        return True
    
# Time Complexity: O(V + E) where V is number of vertices and E is number of edges
# Space Complexity: O(V + E) for storing the graph and visited array    
# Explanation:
# 1. We build a directed graph from the prerequisites list.
# 2. We use Depth First Search (DFS) to detect cycles in the graph.
# 3. We maintain a visited array to keep track of nodes in the current DFS path.
# 4. If we encounter a node that is already visited in the current path, it indicates a cycle, and we return False.
# 5. If we can traverse all nodes without encountering a cycle, we return True, indicating that all courses can be finished.