# Leetcode problem 743: Network Delay Time
# Difficulty : Medium
# URL : https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]
        for i in range(len(times)):
            u,v,w = times[i]
            graph[u].append((v,w))
        # for row in graph:
        #     print(row)
        visited = [0]*(n+1)
        distance = [float('inf')]*(n+1)
        p = []
        heapq.heappush(p,(0,k))
        distance[k] = 0
        while(p):
            w,d = heapq.heappop(p)
            
            if(not visited[d]):
                visited[d] = 1
                for neigh in graph[d]:
                    dst, weight = neigh
                    if(w+weight < distance[dst]):
                        distance[dst] = w+weight
                        heapq.heappush(p,(w+weight,dst))
        maximum = 0
        
        for i in range(1,len(distance)):
            maximum = max(maximum, distance[i])
            if(distance[i] == float('inf')):
                return -1
        return maximum
    
# Time Complexity : O(E log V) where E is the number of edges and V is the number of vertices.
# Space Complexity : O(V) for the distance and visited arrays, and O(E) for the graph representation.   
# Explanation:
# 1. We represent the graph using an adjacency list.
# 2. We use Dijkstra's algorithm to find the shortest path from the starting node `k` to all other nodes.
# 3. We maintain a priority queue to explore the nodes with the smallest distance first.
# 4. We update the distances of the neighboring nodes if we find a shorter path.
# 5. Finally, we check the maximum distance from the starting node to all other nodes. If any node is unreachable, we return -1; otherwise, we return the maximum distance.