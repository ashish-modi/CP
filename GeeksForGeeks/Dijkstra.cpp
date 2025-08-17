// Dijkstra's Algorithm for finding the shortest path in a graph
// This implementation uses a priority queue to efficiently get the next node with the smallest distance.
// https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1

class Solution {
  public:
    vector<int> dijkstra(int V, vector<vector<int>> &edges, int src) {
        // Code here
        vector<int> cost (V, 1e9);
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
        pq.push({0,src});
        cost[src] = 0;
        int min_index = src;
        vector<vector<pair<int,int>>> graph(V);
        for(auto edge : edges){
            int n1 = edge[0];
            int n2 = edge[1];
            int wt = edge[2];
            graph[n1].push_back({wt, n2});

        }
        int count = 0;
        while(!pq.empty()){
            pair<int,int> p = pq.top();
            pq.pop();
            int curr_dist = p.first;
            int node = p.second;

            for(auto it: graph[node]){
                    int wt = it.first;
                    int dest = it.second;
                    int new_dist = curr_dist + wt;
                    if(cost[dest] > new_dist){
                        cost[dest] = new_dist;
                        pq.push({new_dist, dest});
                }
            }
        }
        return cost;
    }
};

// Time Complexity: O((V + E) log V), where V is the number of vertices and E is the number of edges.
// Space Complexity: O(V + E) for storing the graph and the priority queue.