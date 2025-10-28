# Leetcode Problem 332: Reconstruct Itinerary
# Difficulty: Hard
# Link: https://leetcode.com/problems/reconstruct-itinerary/

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        length = len(tickets)
        graph = {}
        result = []
        for i in range(length):
            graph[tickets[i][0]] = []
            graph[tickets[i][1]] = []
        
        for i in range(length):    
            graph[tickets[i][0]].append(tickets[i][1])
        for ele in graph:
            graph[ele].sort(reverse=True)

        def dfs(node):
            while graph[node]: 
                next_node = graph[node].pop()
                dfs(next_node)
            result.append(node)
        
        dfs("JFK")
        
        return result[::-1]

# Time Complexity: O(E log E) where E is the number of edges (tickets). Sorting the adjacency list takes O(E log E) time.
# Space Complexity: O(V + E) where V is the number of vertices (airports) and E is the number of edges (tickets). The graph and the recursion stack take up this space.
# Explanation: The solution constructs a directed graph from the list of tickets, where each airport is a node and each ticket is a directed edge. 
# It then performs a depth-first search (DFS) starting from "JFK", ensuring that it always visits the lexicographically smallest airport next by sorting the adjacency lists in reverse order. 
# The itinerary is built in reverse order during the DFS traversal and is reversed before returning to get the correct order.
