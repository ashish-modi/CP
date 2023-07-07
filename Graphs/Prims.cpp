// Prim's Practice

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