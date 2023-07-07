#include<iostream>
#include<vector>
#include<queue>

using namespace std;

struct triple{
    int weight;
    int n1;
    int n2;
};

class my_function
{
    public:
    int operator()(struct triple &t1, struct triple &t2)
    {
        return t1.weight < t2.weight;
    }
};

int main()
{
    int N, E, n1, n2, w;
    cout << "Enter the number of nodes : ";
    cin >> N;
    cout << "Enter the number of edges : ";
    cin >> E;
    
    priority_queue<struct triple, vector<struct triple>, my_function>  pq;
    vector<int> visited(N);
    vector<pair<int,int>> Edges;

    for(int i = 0 ; i < E ; i++ )
    {
        cin >> n1 >> n2 >> w;
        pq.push({w, n1, n2});
    }

    while(!pq.empty())
    {
        cout << " Weight : " << pq.top().weight << endl;
        pq.pop();
    }
    // Kruskal's algorithm

    while(!pq.empty())
    {
        int node1 = pq.top().n1;
        int node2 = pq.top().n2;
        if(visited[node1] && visited[node2])
            pq.pop();
        else
        {
            visited[node1] = 1;
            visited[node2] = 1;
            Edges.push_back({node1, node2});
        }
    }

 //   for(auto it: Edges)
   //     cout << it.first << "  " << it.second << endl;
    //return 0;
}