#include<iostream>
#include<vector>

using namespace std;

int fun(int M, int N, vector<vector<int>> &maze, vector<vector<int>> &dp)
{ 
    if(dp[M][N] == -2)
    {
        if(maze[M][N] == -1)
        {
            dp[M][N] = 0;
            return dp[M][N];
        }
        else
        {
            int a = 0, b = 0;
            if(dp[M-1][N] == -2)
                a = fun(M -1 , N, maze, dp);
            else
                a = dp[M-1][N];

            if(dp[M][N-1] == -2)
                b = fun(M, N -1, maze, dp);
            else
                b = dp[M][N-1];
            dp[M][N] = a + b;
            return dp[M][N];
        }
    }
    return dp[M][N];
}

int main()
{
    int T;
    cin >> T;
    for( int z = 0 ;z < T ; z++)
    {
        int M, N;
        cin >> M >> N;

        vector<vector<int>> dp(M, vector<int>(N, -2)), maze(M, vector<int>(N));

        for(int i = 0 ; i < M; i++)
        {
            for(int j= 0 ; j < N; j++)
                cin >> maze[i][j];
        }

        int flag = 0;
        for(int i = 0; i < M; i++)
        {
            if(maze[i][0] == -1)
                flag = 1;
            if(flag)
                dp[i][0] = 0;
            else
                dp[i][0] = 1;
        }
        flag = 0;
        for(int i = 0 ; i < N ; i++)
        {
            if(maze[0][i] == -1)
                flag = 1;
            if(flag)
                dp[0][i] = 0;
            else
                dp[0][i] = 1;
        }

        cout << fun(M-1, N-1, maze, dp);
        cout << endl << endl;

        for(int i = 0; i < M; i++)
        {
            for(auto it: dp[i])
                cout << it << " ";
            cout << endl;
        }
    }
    return 0;
}