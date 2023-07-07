// only for directed graphs


#include<iostream>
#include<vector>
using namespace std; 

struct triple{
    int node1;
    int node2;
    int dist;
};

int main()
{
    int N, E, source, n1, n2, w;

    cout << "Enter the number of nodes : ";
    cin >> N;
    cout << "Enter the number of edges : ";
    cin >> E;
    cout << "Enter the source node : ";
    cin >> source;

    vector<triple> Edges;
    int distance[N];
    
    for(int i = 0 ; i < E; i++)
    {
        cin >> n1 >> n2 >> w;
        Edges.push_back({n1,n2,w});
    }

    // distance array
    for(int i= 0 ; i < N; i++)
        distance[i] = 1e9;
    distance[source] = 0;

    for(int i= 0 ; i < N ; i++)
    {
        for(auto it:Edges)
        {
            int new_dist = distance[it.node1] + it.dist;
            if(distance[it.node2] > new_dist)
                distance[it.node2] = new_dist;
        }
    }

    for(auto it: distance)
        cout << it << " " ;
    cout << endl;
    return 0;
}