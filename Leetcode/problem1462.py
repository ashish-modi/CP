# Leetcode problem 1462: Course Schedule IV
# Difficulty : Medium
# Url : https://leetcode.com/problems/course-schedule-iv/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {i:[] for i in range(numCourses)}
        result = [False]*len(queries)

        for i in range(len(prerequisites)):
            graph[prerequisites[i][0]].append(prerequisites[i][1])
        # print("Graph : ", graph)

        def bfs(start, target):
            queue = deque()
            queue.append(start)
            visited = {i: False for i in range(numCourses)}
            visited[start] = True
            while(queue):
                element = queue.popleft()
                for neigh in graph[element]:
                    if(not visited[neigh]):
                        visited[neigh] = True
                        queue.append(neigh)
                        if(neigh == target):
                            return True
            else:
                return False

        for i in range(len(queries)):
            result[i] = True if bfs(queries[i][0], queries[i][1]) else False
        return result
    
# Time complexity : O(n * (V + E)), where n is the number of queries, V is the number of courses and E is the number of prerequisites.
# Space complexity : O(V + E), where V is the number of courses and E is the number of prerequisites.
# Explanation : We can represent the courses and their prerequisites as a directed graph. 
# We can then use breadth-first search (BFS) to check if there is a path from the source course to the target course.