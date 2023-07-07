// Using heap data structure


#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;


int main()
{
    int N, E, n1, n2, w, source;
    cout << "Enter the number of nodes : ";
    cin >> N;
    cout << "Enter the number of edges : ";
    cin >> E;
    cout << "Enter source node: ";
    cin >> source;


    vector<pair<int,int>> v[N];
    vector<pair<int,int>> Nodes;
    pair<int,int> P, pr;

    for(int i = 0 ; i < E ; i++ )
    {
        cin >> n1 >> n2 >> w;
        P = make_pair(w,n2);
        v[n1].push_back(P);
        P = make_pair(w,n1);
        v[n2].push_back(P);
    }

    // displaying the adjacency list

    for(int i =  0 ; i < N; i++)
    {
        for(auto it:v[i])
            cout << it.first << " " << it.second << " ";
        cout << endl;
    } 

    pr = make_pair(0,source);
    Nodes.push_back(pr);

    for(int i= 0; i < N ; i++)
    {
        if(i != source)
        {
            pr = make_pair(numeric_limits<int>::max(), i);
            Nodes.push_back(pr);
        }
    }
/*
    for(auto it:Nodes)
    {
        cout << "Weight " << it.first << endl;
        cout << "Node " << it.second << endl;
    }
*/
   make_heap(Nodes.begin(),Nodes.end());
   sort_heap(Nodes.begin(),Nodes.end());

    // Because of the above statement, Nodes became a heap data structure
    while(! Nodes.empty())
    {
        cout << "Weight : " << Nodes.front().first << endl;
        cout << "Node : " << Nodes.front().second << endl;


        
        pop_heap(Nodes.begin(), Nodes.end()); 
        Nodes.pop_back();
    }
    

    return 0;
}
