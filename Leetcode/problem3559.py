# Leetcode problem 3559: Number of Ways to Assign Edge Weights 2
# Difficulty: Hard
# URL : https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        length = len(edges)
        n_nodes = length + 1

        LOG = math.ceil(math.log2(n_nodes))   
        visited = [0] * (n_nodes + 1)
        graph = {}
        dp = [[0] * (n_nodes + 1) for _ in range(LOG + 1)]  
        depth = [0] * (n_nodes + 1)
        mod_val = 10**9 + 7
        result = deque()

        pow2 = [1] * (n_nodes + 1)
        for i in range(1, n_nodes + 1):
            pow2[i] = (pow2[i-1] * 2) % mod_val


        for edge in edges:
            if(graph.get(edge[0],0)):
                graph[edge[0]].append(edge[1])
            else:
                graph[edge[0]] = [edge[1]]
            if(graph.get(edge[1],0)):
                graph[edge[1]].append(edge[0])
            else:
                graph[edge[1]] = [edge[0]]

        def dfs(node):
            for neigh in graph[node]:
                if(not visited[neigh]):
                    visited[neigh] = True
                    dp[0][neigh] = node
                    depth[neigh] = depth[node] + 1
                    dfs(neigh)
        visited[1] = True
        dfs(1)
        for i in range(1,LOG):
            for j in range(2,length+2):
                dp[i][j] = dp[i-1][dp[i-1][j]]
        result = []
        
        def lift(node, k):
            a = k
            for i in range(LOG, -1,-1):
                if( (1 << i) & k):
                    node = dp[i][node]
            return node
        

        for query in queries:
            a = query[0]
            b = query[1]
            path_length = 0
            
            if(depth[a] > depth[b]):
                path_length += depth[a] - depth[b]
                a = lift(a, depth[a] - depth[b])
            else:
                path_length += depth[b] - depth[a]
                b = lift(b, depth[b]-depth[a])
            
            if(a == b):
                ans = pow2[path_length - 1] if path_length else 0
                result.append(ans)
                continue
            
            for i in range(LOG, -1,-1):
                if(dp[i][a] != dp[i][b]):
                    a = dp[i][a]
                    b = dp[i][b]
                
            lca = dp[0][a]
            path_length = depth[query[0]] + depth[query[1]] - 2*depth[lca]
            ans = pow2[path_length - 1] if path_length else 0
            result.append(ans)
        return list(result)

# Time complexity: O((N + Q) log N) where N is the number of nodes and Q is the number of queries
# Space complexity: O(N log N) for the ancestor table and O(N) for the graph and other arrays   