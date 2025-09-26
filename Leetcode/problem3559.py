class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        length = len(edges)
        length_q = len(queries)
        graph = {}
        for edge in edges:
            if(graph.get(edge[0],0)):
                graph[edge[0]].append(edge[1])
            else:
                graph[edge[0]] = [edge[1]]
            if(graph.get(edge[1],0)):
                graph[edge[1]].append(edge[0])
            else:
                graph[edge[1]] = [edge[0]]

        def bfs(start,end):
            queue = deque()
            queue.append(start)
            visited = [0]*(length + 2)
            visited[start] = level_elements = 1
            new_element = levels = 0
            if(start == end):
                return 0
            print("Visited start : ", visited)
            while(queue):
                element = queue.popleft()
                print("Element : ", element)
                level_elements -=1
                for neigh in graph[element]:
                    if(neigh == end):
                        print("Levels : ", levels+1, "start : ", start)
                        return levels +1
                    if not visited[neigh]:
                        visited[neigh] = 1
                        queue.append(neigh)
                        new_element +=1
                if(level_elements == 0):
                    levels +=1
                    level_elements = new_element
                    new_element = 0
                print("Visited : ", visited)
                
        result = []
        for query in queries:
            start = query[0]
            end = query[1]
            levels = bfs(start, end)
            print("query: ", query, "levels : ", levels)
            ans = 2**(levels-1) if levels > 0 else 0
            result.append(ans)
        return result