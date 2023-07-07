// Graph Representation ( adjacency list using map )

#include<iostream>
#include<map>
#include<vector>
using namespace std;

int main()
{
    int N,E,n1,n2; 
    cout << "Enter number of nodes: ";
    cin >> N;
    cout << "Enter number of edges: ";
    cin >> E;

    map<int,vector<int>> Edges;

    for( int i= 0; i < E; i ++)
    {
        cin >> n1 >> n2;
        Edges[n1].push_back(n2);
        Edges[n2].push_back(n1);
    }

// To traverse a vector, we always need to traverse with the help of iterator

    vector<int>::iterator iter1;
    map<int,vector<int>>::iterator iter2;

    
        for(iter2 = Edges.begin() ; iter2 != Edges.end() ; iter2++)
        {    for(iter1 = (*iter2).second.begin() ; iter1 != (*iter2).second.end() ; iter1++) 
                cout << *iter1 << " ";
                cout<< endl;
        } 
    return 0;
}