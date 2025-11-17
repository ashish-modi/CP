// Leetcode Problem 785 : Is graph bipartite ? 
// Difficulty: Medium
// https://leetcode.com/problems/is-graph-bipartite/


class Solution {
public:
    void bfs(vector<vector<int>> &graph, vector<int> &colour, vector<int> &visited, int source, bool & flag){
        colour[source] = 1;
        visited[source] = 1;
        queue<int> q;
        q.push(source);
        while(!q.empty()){
            int node = q.front();
            q.pop();
            int node_colour = colour[node];
            int neighbour_colour = node_colour== 1? 2: 1;
            for(auto element : graph[node]){
                // cout << " node : " << node << " Neighbour : " << element << "  NC : " << neighbour_colour << endl;
                if(colour[element] == node_colour){
                    flag = false;
                    return;
                }
                if(!visited[element]){
                    q.push(element);
                    colour[element] = neighbour_colour;
                    visited[element] = 1;
                }
            }

        }
        flag = true;
    }

    bool isBipartite(vector<vector<int>>& graph) {
        int nodes = graph.size();
        vector<int> colour(nodes, -1), visited(nodes, 0);
        bool flag = true;
        for(int i = 0; i < nodes; i++){
            if(visited[i] == 0){
                bfs(graph, colour, visited, i, flag);
                if(flag == false)
                    return flag;
            }
        }
        return flag;
    }
};

// Time Complexity : O(V + E) where V is the number of vertices and E is the number of edges in the graph.
// Space Complexity : O(V) for the colour and visited arrays.
// Explanation:
// 1. We define a BFS function that takes the graph, colour array, visited array, source node, and a flag as input.
// 2. We initialize the colour of the source node to 1 and mark it as visited.
// 3. We use a queue to perform BFS traversal of the graph.
// 4. For each node, we check its neighbours. If a neighbour has the same colour as the current node, we set the flag to false and return.
// 5. If a neighbour is not visited, we assign it the opposite colour and mark it as visited.
// 6. In the main function, we iterate through all nodes and call the BFS function for unvisited nodes.
// 7. If the flag is false at any point, we return false; otherwise, we return true indicating the graph is bipartite.