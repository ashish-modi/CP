# For finding the LCA of two nodes in a tree using Binary Lifting
# Time Complexity: O(N log N) for preprocessing, O(log N) for each LCA query
# Space Complexity: O(N log N) for storing the ancestor table   

# Key Idea of Binary Lifting
# Precompute up[k][v]: the 2^k-th ancestor of node v.

# up[0][v] = parent of v
# up[1][v] = 2nd ancestor (parent of parent)
# up[2][v] = 4th ancestor, etc.

# Precompute depths via DFS.

# To find LCA(u, v):
# Lift the deeper node up until both are at the same depth.
# Lift them together (largest powers first) until their parents are equal.

import math
from typing import List

class BinaryLiftingLCA:
    def __init__(self, n: int, edges: List[List[int]], root: int = 1):
        self.n = n
        self.LOG = math.ceil(math.log2(n))
        self.graph = [[] for _ in range(n+1)]
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)

        self.up = [[0]*(n+1) for _ in range(self.LOG+1)]  # up[k][v] = 2^k ancestor of v
        self.depth = [0]*(n+1)

        # Preprocess
        self.dfs(root, root)
        for k in range(1, self.LOG+1):
            for v in range(1, n+1):
                self.up[k][v] = self.up[k-1][self.up[k-1][v]]

    def dfs(self, v, p):
        self.up[0][v] = p
        for neigh in self.graph[v]:
            if neigh != p:
                self.depth[neigh] = self.depth[v] + 1
                self.dfs(neigh, v)

    def lift(self, v, k):
        for i in range(self.LOG, -1, -1):
            if (k >> i) & 1:
                v = self.up[i][v]
        return v

    def lca(self, u, v):
        if self.depth[u] < self.depth[v]:
            u, v = v, u  # ensure u is deeper
        # 1) Lift u up to same depth as v
        u = self.lift(u, self.depth[u] - self.depth[v])

        if u == v:
            return u

        # 2) Lift u and v together until their parents are same
        for i in range(self.LOG, -1, -1):
            if self.up[i][u] != self.up[i][v]:
                u = self.up[i][u]
                v = self.up[i][v]

        # 3) Their parent is the LCA
        return self.up[0][u]
# Example usage:
# edges = [[1, 2], [1, 3], [2, 4], [2, 5]]
# lca_finder = BinaryLiftingLCA (n=5, edges=edges, root=1)
# print(lca_finder.lca(4, 5))  # Output: 2
# print(lca_finder.lca(4, 3))  # Output: 1
# print(lca_finder.lca(2, 3))  # Output: 1
# The above class can be used to preprocess a tree and answer LCA queries efficiently.  