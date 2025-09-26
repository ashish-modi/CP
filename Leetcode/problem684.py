# Leetcode Problem : Redundant Connection
# Difficulty : Medium
# Link : https://leetcode.com/problems/redundant-connection/
# Based on Union Find Algorithm

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        length = len(edges)
        p = []
        parent = [i for i in range(length+1)]
        def find_parent(node):
            while parent[node] != node:
                node = parent[node]
            return node

        for i in range(length):
            s, d = edges[i]
            parent_s = find_parent(s)
            parent_d = find_parent(d)
            if(parent_s != parent_d):
                parent[parent_d] = parent_s
            else:
                return edges[i]

# Time Complexity : O(N * α(N)) where α is the Inverse Ackermann function.
# Space Complexity : O(N) for the parent array. 