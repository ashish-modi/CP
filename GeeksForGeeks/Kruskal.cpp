// Minimum Spanning Tree using Kruskal's Algorithm
// Difficulty Level: Medium
// Problem Link: https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1

class Solution {
  public:
    struct Edge{
      int node1, node2, weight;
    };
    
    struct myComparator{
      bool operator()(Edge &a, Edge &b){
          return a.weight > b.weight;       // Min-Heap based on weight
      }
    };
    
    vector<int> parent;
    int find(int node){
        while(parent[node] != node){
            node = parent[node];              // Path compression
        }
        return node;
    }
    
    int spanningTree(int V, vector<vector<int>>& edges) {
        // code here
        priority_queue<Edge, vector<Edge>, myComparator> pq;
        parent.resize(V);
        for(int i = 0 ; i < V; i ++) parent[i] = i;
        
        for(auto it: edges){
            int n1 = it[0];
            int n2 = it[1];
            int wt = it[2];
            pq.push({n1,n2,wt});
        }
        int cost = 0;
        while(!pq.empty()){
            Edge it = pq.top();
            pq.pop();
            int n1 = it.node1;
            int n2 = it.node2;
            int wt = it.weight;
            int parent_n1 = find(n1);          // Find the root parent of n1
            int parent_n2 = find(n2);       // Find the root parent of n2
            // cout << "Parent n1 : " << parent_n1 << endl;
            // cout << "Parent n2 : " << parent_n2 << endl;

            // If both nodes have different parents, they are not connected and we can add the edge to the MST
            // Otherwise, adding this edge would create a cycle so we skip it
            // This is the key step in Kruskal's algorithm to ensure we do not form cycles and only add edges that connect disjoint sets
            if(parent_n1 != parent_n2){
                parent[parent_n2] = parent_n1;
                cost += wt;
            }
        }
        return cost;
        
    }
};


// Time Complexity: O(E log E) where E is the number of edges
// Space Complexity: O(V) where V is the number of vertices
// Note: The code uses a priority queue to sort edges by weight and a union-find structure to detect cycles.
// The algorithm efficiently finds the minimum spanning tree of a graph using Kruskal's method.