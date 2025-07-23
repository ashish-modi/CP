// Problem : Is graph bipartite ? (medium)


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