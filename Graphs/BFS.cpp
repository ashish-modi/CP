#include<iostream>
#include<queue>
#include<vector>
using namespace std;


int main()
{

    int N, E, n1, n2, node;
    cout << "Enter the number of nodes : ";
    cin >> N;
    cout << "Enter the number of edges : ";
    cin >> E;

    queue<int> Q;               
    vector<int> v[N+1];          // adjacency list
    vector<int>:: iterator iter;
    vector<int> visited(N+1);    // marking visited nodes
    int starting_node = 6;

    for(int i= 0 ; i < E ; i++)
    {
        cin >> n1 >> n2;
        v[n1].push_back(n2);
        v[n2].push_back(n1);
    }

    // inserting starting node into the queue
    Q.push(starting_node);
    visited[starting_node] = 1;

    while(!Q.empty())
    {
        node = Q.front();                   // taking out the front node
        cout << node << " ";                // print it as it is part of traversal
        Q.pop();

        // traversing all its neighbours

        for(iter=v[node].begin() ; iter != v[node].end() ; iter++)
        {

            // it the neighbour is not visited, add it into the queue and mark as visited
            if( ! visited[*iter])
            {   
                Q.push(*iter);
                visited[*iter] = 1;
            }
                
        }
    } 

}