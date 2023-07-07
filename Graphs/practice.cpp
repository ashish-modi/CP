#include<bits/stdc++.h>

using namespace std;

class my_fun
{
    public:
    int operator()(pair<int,int> p1, pair<int,int> p2)
    {
        return p1.first > p2.first;
    }
};

int main()
{
    int N, E, start;
    cout << "Enter the number of nodes : ";
    cin >> N;
    cout << "Enter the number of edges : ";
    cin >> E;
    cout << "Enter the starting node: ";
    cin >> start;

    int n1, n2, w, node;
    vector<int> distance(N,INT_MAX);
    vector<pair<int,int>> graph[N];
    priority_queue<pair<int,int>, vector<pair<int,int>>, my_fun> pq;

    for(int i = 0 ; i < E; i++)
    {
        cin >> n1 >> n2 >> w;
        graph[n1].push_back({w,n2});
        graph[n2].push_back({w,n1});
    }

    pq.push({0,start});
    int weight, node;
    while(!pq.empty())
    {
        weight = pq.top().first;
        node = pq.top().second;
        for(auto it: graph[node])
        {
            int new_weight = weight + it.first;
            if(distance[it.second] > new_weight)
            {
                distance[it.second] = new_weight;
                pq.push({new_weight, it.second});
            }
        }
        pq.pop();
    }
    return 1;
}