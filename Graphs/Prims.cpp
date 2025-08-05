// Prim's Practice

// Creates min heap
// priority_queue<int, vector<int>, greater<int>> minHeap;      


#include<bits/stdc++.h>

using namespace std;


struct triple
{
    int weight;
    int child;
    int parent;
};

// comparator class for priority queue ( OPERATOR function is being overloaded)
class my_fun
{
    public:
    int operator()(struct triple &t1, struct triple &t2)
    {
        return t1.weight > t2.weight;
    }
};


int main()
{
    int N, E, source;

    cout << "Enter the number of nodes : ";
    cin >> N;
    cout << "Enter the number of edges : ";
    cin >> E;
    cout << "Enter the source node : ";
    cin >> source;

    vector<pair<int,int>> adj[N], Edges;               // adjacency list
    priority_queue<struct triple,vector<struct triple>,my_fun> pq;          // priority queue
    vector<int> visited(N);                    // visited array                                   

    int n1, n2 , w;

    // storing edges as adjacency list

    for(int i = 0 ; i < E ; i++)
    {
        cin >> n1 >> n2 >> w;
        adj[n1].push_back({w, n2});
        adj[n2].push_back({w, n1});
    }

    pq.push({0,source,-1});
    int min_sum = 0;   
    // prim's algorithm
    
    while(!pq.empty())
    {
        int child = pq.top().child;
        int parent = pq.top().parent;
        
        // take the edge with the minimum weight and then travese all its neighbours

        if(!visited[child])
        {
            if(parent != -1)
            {
                min_sum += pq.top().weight;
                Edges.push_back({child,parent});         // Storing the edge which is part of MST
            }
    
    // pop the minimum node from the min heap because it can change after new nodes are added
            pq.pop();
            visited[child] = 1;

    // traversing all the neighbours 
            for(auto it: adj[child])
            {
                if(!visited[it.second])
                    pq.push({it.first, it.second, child});
            }

        }
        else
            pq.pop();
    }

    for(auto it: Edges)
        cout << it.first << "    " << it.second << endl;
    
    cout << "SUM : " << min_sum << endl;

}


// Geeks for Geeks (Minimum Spanning Tree (Medium))

// Given a weighted, undirected, and connected graph with V vertices and E edges,
//  your task is to find the sum of the weights of the edges in the Minimum Spanning Tree (MST) 
// of the graph. The graph is represented by an adjacency list, where each element adj[i] is a vector containing vector of integers.
//  Each vector represents an edge, with the first integer denoting the endpoint of the edge and the second integer denoting the weight of the edge.

// Input:
// 3 3
// 0 1 5
// 1 2 3
// 0 2 1

class Solution {
  public:
    struct CompareByWeight {
    bool operator()(const pair<int, int>& a, const pair<int, int>& b) {
        return a.second > b.second; // min-heap by .second (weight)
    }
};
    int spanningTree(int V, vector<vector<int>> adj[]) {
        // code here
        vector<int> visited (V,0);
        int start = 0;
        priority_queue<pair<int,int>, vector<pair<int,int>>, CompareByWeight> pq;
        pq.push({0,0});
        int cost =0;
        while(!pq.empty()){
            pair<int,int> it = pq.top();
            int wt = it.second;
            int node = it.first;
            pq.pop();
            // cout << " NODE : " << node << endl;
            if(!visited[node]){
                visited[node] = 1;
                cost += wt;
                vector<vector<int>> row = adj[node];
                for(vector<int> pairs : row){
                        pq.push({pairs[0],pairs[1]});
                }
            }
            // auto temp = pq;

            // while (!temp.empty()) {
            //     pair<int,int> it = temp.top();
            //     cout << it.first << " " << it.second << endl;
            //     temp.pop();
            // cout << " Visited : " << endl;
            // for(auto it : visited)
            //     cout << it << " ";
            // cout << endl;
            // }
        }
        return cost;
    }
};
     
     
     
     
     
     
//         for (int i = 0; i < V; ++i) {
//             cout << "adj[" << i << "]:" << endl;
//             for (auto &vec : adj[i]) {
//                 for (int val : vec) {
//                     cout << val << " ";
//                 }
//                 cout << endl;
//             }
//         }
//     }
// };

