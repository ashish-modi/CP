#include<bits/stdc++.h>

using namespace std;
#include<stack>

void dfs(int node, vector<vector<int>> &graph, vector<int> &visited, stack<int> &s)
{
    visited[node] = 1;
    for(auto it: graph[node])
    {
        if(!visited[it])
            dfs(it, graph, visited, s);
    }
    s.push(node);
}


int main()
{
    int N, E;
    cout << "Enter the number of nodes : " ;
    cin >> N;
    cout << "Enter the number of edges : " ;
    cin >> E;

    vector<vector<int>> graph(N);
    vector<int> visited(N);
    stack<int> s;

    cout << "Enter the edges";
    int n1, n2;
    for(int i = 0; i < E; i++)
    {
        cin >> n1 >> n2;
        graph[n1].push_back(n2);
    }
    for(int i = 0 ; i < N; i++)
    {
        if(!visited[i])
            dfs(i, graph, visited, s);
    }
    while(!s.empty())
    {
        cout << s.top() << " ";
        s.pop();
    }
}