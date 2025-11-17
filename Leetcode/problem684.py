# Leetcode Problem 684: Redundant Connection
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
# Explanation:
# 1. We initialize a parent array where each node is its own parent.
# 2. We define a helper function `find_parent` to find the root parent of a node using path compression.
# 3. We iterate through each edge in the input list.
# 4. For each edge, we find the root parents of both nodes.