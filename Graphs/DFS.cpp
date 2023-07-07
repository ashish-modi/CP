#include<iostream>
#include<vector>
#include<stack>
using namespace std;

int main()
{ 
    int N, E, n1, n2, node, flag;

    cout << "Enter the number of nodes : ";
    cin >> N;
    cout << "Enter the number of edges : ";
    cin >> E;

    vector<int> v[N+1];
    vector<int> visited(N+1);
    stack<int> S;
    vector<int>:: iterator iter;
    int start = 4;

    for(int i = 0 ; i < E; i++)
    {
        cin >> n1 >> n2;
        v[n1].push_back(n2);
        v[n2].push_back(n1);
    }

    S.push(start);
    visited[start] = 1;
    cout << start << " ";

    while( ! S.empty())
    {
        node = S.top();
        flag = 0;
        
        for(iter = v[node].begin() ; iter != v[node].end(); iter++)
        {
            if(!visited[*iter])
            {
                visited[*iter] = 1;
                S.push(*iter);
                cout << S.top() << " ";
                flag = 1;
                break;
            }
        }
        if(!flag)
            S.pop();
    }
}