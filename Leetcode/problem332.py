class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        length = len(tickets)
        graph = {}
        visited = {}
        result = []
        for i in range(length):
            graph[tickets[i][0]] = []
            graph[tickets[i][1]] = []
        for i in range(length):    
            graph[tickets[i][0]].append([tickets[i][1],0])
        for ele in graph:
            graph[ele].sort()
        def dfs(node):
            visited[node] = 1
            result.append(node)
            for ele in graph[node]:
                if(ele[1] == 0):
                    ele[1] = 1
                    dfs(ele[0])
        
        print(graph)
        dfs("JFK")
        print("Result :", result)
        return result