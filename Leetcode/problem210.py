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
# Explanation:
# 1. We build a directed graph from the prerequisites list.
# 2. We use Depth First Search (DFS) to detect cycles in the graph and build the course order.
# 3. We maintain a visited array to keep track of nodes in the current DFS path.
# 4. If we encounter a node that is already visited in the current path, it indicates a cycle, and we return an empty list.
# 5. If we can traverse all nodes without encountering a cycle, we append the nodes to the answer list in post-order.
# 6. Finally, we return the course order, appending any courses that were not part of the prerequisites.