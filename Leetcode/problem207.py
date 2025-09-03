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
