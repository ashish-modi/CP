#include<bits/stdc++.h>

using namespace std;

int main()
{ 
    string S ="HEaLLOh123@";
    map<char,int> count;
    for(int i = 0 ; i < S.size() ; i++)
    {   
        cout << "Type of : " << S[i] << "  " << isalpha(S[i]) << endl;
        count[S[i]] +=1;
    }


    for(auto it: count)
    {
        cout << it.first << " " << it.second << endl;
    }
}