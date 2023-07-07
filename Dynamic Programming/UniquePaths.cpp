#include<iostream>
#include<vector>

using namespace std;

int fun(int M, int N, vector<vector<int>> &dp)
{ 
    if(dp[M][N] == -1)
    {
        if(N == 0 || M == 0)
        {
            dp[M][N] = 1;
            return dp[M][N];
        }
        else
        {
            int a = 0, b = 0;
            if(dp[M-1][N] == -1)
                a = fun(M-1, N, dp);
            else
                a = dp[M-1][N];
            if(dp[M][N-1] == -1)
                b = fun(M, N - 1, dp);
            else
                b = dp[M][N-1];
            dp[M][N] = a+b;
            return dp[M][N];
        }
    }
    return dp[M][N];
}

int main()
{
    int T;
    cin >> T;
    for(int z = 0 ; z< T ; z++)
    {
        int M,N;
        cin >> M >> N ;
        vector<vector<int>> dp(M, vector<int>(N,-1));
        cout << " ANSWER : "<< fun(M -1 ,N -1,dp) << endl;
        for(int i = 0; i < M; i++)
        {
            for(auto it: dp[i])
                cout << it << " ";
            cout << endl;
        }

    }
    return 0;
}