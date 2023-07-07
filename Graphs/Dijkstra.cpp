// Using priority queue as a min heap


#include<iostream>
#include<vector>
#include<queue>
using namespace std;


int main()
{ 
    int N, E, source, n1, n2, w;
    cout << "Enter the number of node: ";
    cin >> N;
    cout << "Enter the number of edges : ";
    cin >> E;
    cout << "Enter the source node: ";
    cin >> source;

    vector<pair<int,int>> Nodes[N];
    vector<pair<int,int>> ::iterator iter;
    // pair<int,int> P;

// greater is a predefined comparator which gives priority to the smallest element first 
    // and acts like a min heap

    priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> pq;
    int distance[N];

    for(int i= 0; i < E ; i++)
    {
        cin >> n1 >> n2 >> w;
        //P = make_pair(w,n1);
        Nodes[n2].push_back({w,n1});
        //P = make_pair(w,n2);
        Nodes[n1].push_back({w,n2});
    }

    for(int i=0; i<N ; i++)
        distance[i] = 1e9;             // 1e9 means 10 to the power 9
    distance[source] = 0;

    pq.push({0,source});

    int node, dist, new_dist;
    while(!pq.empty())
    {
        dist = pq.top().first;
        node = pq.top().second;
        pq.pop();

     
        for(auto it:Nodes[node])
        {
            new_dist = dist + it.first;
            if(new_dist < distance[it.second])
            {
                distance[it.second] = new_dist;
                pq.push({new_dist, it.second});
            }
        }
    }

    for(auto it:distance)
        cout << it << " " ;
    return 0;
}