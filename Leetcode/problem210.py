# Porblem 210: Course Schedule II
# Difficulty: Medium
# https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        length = len(prerequisites)
        visited = [False]*numCourses
        for edge in prerequisites:
            graph[edge[0]].append(edge[1])
        answer = []
        
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
            answer.append(start)
            return True

        for i in range(length):
            if(not done[prerequisites[i][0]]):
                if(not dfs(prerequisites[i][0])):
                    return []
                else:
                    visited[prerequisites[i][0]] = False
        extra = []
        for i in range(numCourses):
            if(done[i] == False):
                extra.append(i)
        return answer+extra if prerequisites else extra

# Time Complexity: O(V + E) where V is number of vertices and E is number of edges
# Space Complexity: O(V + E) for storing the graph and visited array    