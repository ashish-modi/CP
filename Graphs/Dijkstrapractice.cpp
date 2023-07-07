#include<bits/stdc++.h>

using namespace std;

class my_fun
{
    public:
    int operator()(pair<int,int> &p1, pair<int,int> &p2)
    {
        return p1.first > p2.first;
    }
};


void fun(int source, priority_queue<pair<int,int>,vector<pair<int,int>>, my_fun> &pq, vector<int> &dist, vector<pair<int,int>> *adj)
{
    dist[source] = 0;
    pq.push({0,source});

    while(!pq.empty())
    {
        int node = pq.top().second;

        for(auto it: adj[node])
        {
            int new_weight = pq.top().first + it.first;
            if(new_weight < dist[it.second])
            {
                dist[it.second] = new_weight;
                pq.push({new_weight, it.second});
            }
        }
        pq.pop();
    }
}


int main()
{
    int N, E, source;
    cout << "Enter the number of nodes: ";
    cin >> N;
    cout << " Enter the number of edges : ";
    cin >> E;
    cout << "Enter the source node: ";
    cin >> source;


    priority_queue<pair<int,int>, vector<pair<int,int>>, my_fun> pq;
    vector<pair<int,int>> adj[N];
    vector<int> dist(N, INT_MAX);
    int n1, n2, w;

    for(int i = 0 ; i < E; i++)
    {
        cin >> n1 >> n2 >> w;
        adj[n1].push_back({w,n2});
        adj[n2].push_back({w,n1});
    }

    fun(source, pq, dist, adj);
    for(auto it: dist)
        cout << it << " " ;   
}