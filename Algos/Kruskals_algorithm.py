# Kruskal's algorithm
# URL : https://leetcode.com/problems/min-cost-to-connect-all-points/description/


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        length = len(points)
        p = []
        parent = {}
        result = total = 0
        for i in range(length):
            for j in range(i+1,length):
                src = points[i]
                dst = points[j]
                if(not parent.get((src[0],src[1]), 0)):
                    parent[(src[0],src[1])] = (src[0],src[1])
                if(not parent.get((dst[0],dst[1]), 0)):
                    parent[(dst[0], dst[1])] = (dst[0],dst[1])
                val = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                
                heapq.heappush(p,(val,(src[0],src[1]), (dst[0],dst[1])))
        
        def find_parent(node):
            if(parent[node] != node):
                node = find_parent(parent[node])
            return node
        
        while(p):
            value, source, destination = heapq.heappop(p)
            
            parent_src = find_parent(source)
            parent_dst = find_parent(destination)
            if(parent_src != parent_dst):
                parent[parent_dst] = parent_src
                result += value
                total +=1
                if(total == length-1):
                    break
            
        return result
            

# Time complexity : O(ElogE) where E is the number of edges in the graph
# Space complexity : O(E) for storing the edges and O(V) for the parent array
# Explanation : Kruskal's algorithm is a greedy algorithm used to find the minimum spanning tree of a graph. 
# It works by sorting all the edges in non-decreasing order of their weights and then adding them one by one to the spanning tree, ensuring that no cycles are formed. 
# The algorithm uses a union-find data structure to keep track of the connected components and to efficiently check for cycles.