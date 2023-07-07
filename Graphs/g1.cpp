// Graph Representation ( adjacency list using vectors )

#include<iostream>
#include<map>
#include<vector>
#include<list>

using namespace std;
int main()
{
    
    int N,E,n1,n2;
    cout << "Enter number of nodes : ";
    cin >> N;
    cout << "Enter number of edges : ";
    cin >> E;

    vector<int> Edges[N+1];

    for(int i=0 ; i<E ; i++)
    {
        cin >> n1 >> n2;
        Edges[n1].push_back(n2);
        Edges[n2].push_back(n1);
    }
    vector<int>::iterator iter;
    for(int i = 0;i < N + 1; i++)
    {
        cout <<i<<"->"; 
        for( iter= Edges[i].begin(); iter != Edges[i].end(); iter ++)
            cout << (*iter) << " ";
        cout << endl;
    }

    return 0;
}