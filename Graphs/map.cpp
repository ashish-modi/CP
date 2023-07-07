#include<iostream>
#include<map>
#include<vector>

using namespace std;


void display(map<int,char> M)
{ 
    for(auto iter: M)        // iter is the iterator for map M
    {
        // key can be accessed using iter.first
        // value can be accessed using iter.second

        cout << iter.first << "-->" << iter.second << endl;     
    }
}


int main()
{
    int N, k;
    char v;
    map <int,char> E;
    cout << "Enter the number of (key,value) to enter: ";
    cin >> N;
    for(int i=0 ; i < N; i++)
    {
            cin >> k >> v;
            E[k] = v;
    }
    cout << endl << "Size of map is: " << E.size() << endl;



    // using the iterator to display all the elements of the map
    
    map<int, char>:: iterator iter1;

    for(iter1 = E.begin() ; iter1 != E.end() ; iter1++)
    {
        cout << (*iter1).first << "--> " << (*iter1).second << endl; 
    }

    return 0;
}