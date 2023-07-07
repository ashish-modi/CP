#include<iostream>
#include<vector>
#include<bits/stdc++.h>

using namespace std;

int fun(int N, int c,vector<vector<int>> &train, vector<vector<int>> &dp)
{ 
    if(dp[N][c] == 0)
    {
        if(N== 0)
        {
            int m = 0;
            for(int i = 0 ; i < 3; i++)
            {
                if(i != c)
                    m = max(m,train[N][i]);
            }
            return m;
        }
        else
        {
            int a, maximum = 0;
            // selected the element at train[N][c]
            for(int i = 0 ; i < 3; i++)
            {
                if( i != c)
                {
                    if(dp[N-1][i] == 0)
                        a = fun(N -1, i, train, dp);
                    else
                        a = dp[N-1][i];

                    if( a + train[N][i] > maximum)
                        maximum = a + train[N][i];
                }
            }
            dp[N][c] = maximum;
        }
    }
    return dp[N][c];
}



int main()
{
    int T;
    cin >> T;
    for(int z = 0 ; z < T; z++)
    {
        int N, a; 
        cin >> N;

        vector<vector<int>> train(N, vector<int>(N,0));
        vector<vector<int>> dp(N, vector<int>(4,0));    // initializing a 2D vector with all zeros

        for(int i = 0 ; i < N ; i++)
        {
            for(int j = 0 ; j < 3; j++)
            {
                cin >> a;
                train[i][j] = a;
            }
        }

        cout << endl << "ANSWER : " << fun(N - 1, 3, train, dp) << endl;

        cout << endl << "DP : " << endl;
        
        for(int i = 0  ; i < N ; i++)
        {
            for(auto it: dp[i])
                cout << it << " ";
            cout << endl;
        }
    }
    return 0;
}