# Leetcode Problem 1584: Min Cost to Connect All Points
# Difficulty Level : Medium
# Link : https://leetcode.com/problems/min-cost-to-connect-all-points/

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
            while(parent[node] != node):
                node = parent[node]
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
        
# Time Complexity : O(E log E) where E is number of edges
# Space Complexity : O(E) where E is number of edges    
# Explanation:
# 1. We create a list of all edges with their corresponding Manhattan distances.
# 2. We use a priority queue (min-heap) to always expand the least costly edge.
# 3. We use the Union-Find data structure to keep track of connected components and avoid cycles.
# 4. We continue adding edges until we have connected all points (length - 1 edges).
        